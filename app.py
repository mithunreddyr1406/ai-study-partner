# app.py
import os
import json
import traceback
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()  # loads .env so GROQ_API_KEY can be read

app = Flask(__name__, template_folder="templates", static_folder="static")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
# Use a supported model name you have access to
MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/quiz")
def quiz_page():
    return render_template("quiz.html")


@app.route("/result")
def result_page():
    return render_template("result.html")


@app.route("/api/generate", methods=["POST"])
def generate_quiz():
    """
    Expect JSON body { topic, difficulty, mode }.
    Return JSON: { "questions": [ { "q": ..., "type":"mcq"/"short", "options":[...], "answer": "..." }, ... ] }
    """
    try:
        payload = request.get_json() or {}
        topic = payload.get("topic", "general knowledge")
        difficulty = payload.get("difficulty", "easy")
        mode = payload.get("mode", "practice")  # practice/test/challenge

        # Prompt: ask for strict JSON with answer ALWAYS included (important)
        prompt = f"""
Generate 10 quiz questions on the topic: "{topic}" with difficulty "{difficulty}" for mode "{mode}".
Return VALID JSON only — EXACT format below (no extra prose, no markdown):

{{
  "questions": [
    {{
      "q": "Question text",
      "type": "mcq",
      "options": ["Option A text", "Option B text", "Option C text", "Option D text"],
      "answer": "Option B text"
    }}
  ]
}}

Rules:
- ALWAYS include "answer" and "options" for mcq questions.
- "answer" must exactly match one of the strings in "options".
- If mode == "test", still include "answer" in the JSON (we will hide it in the UI).
- Return exactly one JSON object as above.
"""

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        }

        body = {
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
            "max_tokens": 3000,
        }

        r = requests.post(GROQ_URL, headers=headers, json=body, timeout=30)
        r.raise_for_status()
        result = r.json()

        # Basic validation
        if not result.get("choices"):
            return jsonify({"error": "No choices returned from LLM", "raw": result}), 500

        content = result["choices"][0]["message"]["content"]
        # strip any code fences
        content = content.replace("```json", "").replace("```", "").strip()

        # Attempt to extract JSON block
        try:
            parsed = json.loads(content)
        except Exception:
            # try to find first { ... } or [ ... ] block
            import re
            m = re.search(r"(\{.*\}|\[.*\])", content, re.S)
            if not m:
                return jsonify({"error": "Unable to parse JSON from LLM", "raw": content}), 500
            parsed = json.loads(m.group(0))

        # normalize structure to { "questions": [...] }
        if isinstance(parsed, list):
            questions = parsed
        elif isinstance(parsed, dict) and "questions" in parsed:
            questions = parsed["questions"]
        else:
            return jsonify({"error": "Unexpected JSON structure from LLM", "raw": parsed}), 500

        # final safety: keep only valid questions that have q/options/answer
        out_q = []
        for q in questions:
            q_text = q.get("q") or q.get("question") or None
            opts = q.get("options") or q.get("choices") or []
            ans = q.get("answer") or q.get("correct") or ""
            if not q_text or not isinstance(opts, list) or not ans:
                # skip malformed
                continue
            out_q.append({
                "q": q_text,
                "type": q.get("type", "mcq"),
                "options": opts,
                "answer": ans
            })

        if not out_q:
            return jsonify({"error": "LLM produced no valid questions", "raw": parsed}), 500

        return jsonify({"questions": out_q})

    except Exception as e:
        return jsonify({"error": "server_exception", "message": str(e), "trace": traceback.format_exc()}), 500


@app.route("/api/grade", methods=["POST"])
def grade_quiz():
    """
    Expect JSON body: { questions: [...], answers: [...] }
    Returns: { score, total, details: [ { question, your_answer, correct_answer, is_correct } ] }
    """
    try:
        data = request.get_json() or {}
        questions = data.get("questions") or []
        answers = data.get("answers") or []

        score = 0
        details = []

        for i, q in enumerate(questions):
            q_text = q.get("q") or q.get("question") or "Question not found"
            correct_raw = q.get("answer") or q.get("correct") or ""
            correct_norm = correct_raw.strip().lower()

            # safely get user answer if missing -> ""
            user_raw = answers[i] if i < len(answers) else ""
            user_norm = (user_raw or "").strip().lower()

            is_correct = False
            if correct_norm and user_norm:
                is_correct = (user_norm == correct_norm)
            else:
                # also try to match by letter if options like "A) 4" and user typed "A" or "a"
                # build mapping option-letter -> normalized option text
                opts = q.get("options") or []
                opt_map = {}
                for idx, o in enumerate(opts):
                    letter = chr(65 + idx).lower()  # a,b,c...
                    opt_map[letter] = (o or "").strip().lower()
                    # also map full option text to itself
                    opt_map[(o or "").strip().lower()] = (o or "").strip().lower()

                if user_norm in opt_map and correct_norm in opt_map:
                    is_correct = (opt_map[user_norm] == opt_map[correct_norm])
                else:
                    # fallback: compare text substrings
                    is_correct = (correct_norm != "" and correct_norm in user_norm)

            if is_correct:
                score += 1

            details.append({
                "question": q_text,
                "your_answer": user_raw,
                "correct_answer": correct_raw,
                "is_correct": is_correct
            })

        return jsonify({"score": score, "total": len(questions), "details": details})

    except Exception as e:
        return jsonify({"error": "grading_exception", "message": str(e), "trace": traceback.format_exc()}), 500


if __name__ == "__main__":
    app.run(debug=True)





