# 📚 AI Study Partner

## AI-Powered Personalized Learning and Quiz Generation System

AI Study Partner is a web-based Artificial Intelligence application designed to help students learn and practice academic topics through automatically generated quizzes.

The system allows students to enter a topic, select a difficulty level, and choose the number of questions. The application sends the request to the **Groq API**, which uses an AI language model to generate relevant multiple-choice questions.

The project combines **Python, Flask, HTML, CSS, JavaScript, and Groq API** to provide an interactive and simple learning environment.

---

## 📌 Table of Contents

1. [Project Overview](#1--project-overview)
2. [Problem Statement](#2--problem-statement)
3. [Proposed Solution](#3--proposed-solution)
4. [Objectives](#4--objectives)
5. [Key Features](#5--key-features)
6. [Technologies Used](#6--technologies-used)
7. [Hardware Requirements](#7--hardware-requirements)
8. [Software Requirements](#8--software-requirements)
9. [Program Structure](#9--program-structure)
10. [Description of Program Files](#10--description-of-program-files)
11. [Frontend Structure](#11--frontend-structure)
12. [Project Architecture](#12--project-architecture)
13. [System Modules](#13--system-modules)
14. [System Workflow](#14--system-workflow)
15. [How the Program Works](#15--how-the-program-works)
16. [Groq API Integration](#16--groq-api-integration)
17. [API Key Management](#17--api-key-management)
18. [API Endpoint](#18--api-endpoint)
19. [User Interface](#19--user-interface)
20. [Installation](#20--installation)
21. [Configuration](#21--configuration)
22. [Running the Application](#22--running-the-application)
23. [Testing](#23--testing)
24. [Advantages](#24--advantages)
25. [Limitations](#25--limitations)
26. [Future Enhancements](#26--future-enhancements)
27. [Applications](#27--applications)
28. [Security](#28--security)
29. [Project Input and Output](#29--project-input-and-output)
30. [Expected Application Screens](#30--expected-application-screens)
31. [Learning Outcomes](#31--learning-outcomes)
32. [Concepts Used](#32--concepts-used)
33. [Frontend and Backend Communication](#33--frontend-and-backend-communication)
34. [Complete Technology Stack](#34--complete-technology-stack)
35. [Project Summary](#35--project-summary)
36. [Project Highlights](#36--project-highlights)
37. [Future Vision](#37--future-vision)
38. [Conclusion](#38--conclusion)
39. [Developer](#39--developer)
40. [License](#40--license)

---

## 1. 📖 Project Overview

AI Study Partner is an AI-based educational web application that helps students generate practice quizzes automatically.

Traditional learning systems usually provide fixed questions prepared by teachers or developers. AI Study Partner provides a more flexible approach where questions can be generated dynamically according to the student's selected topic and difficulty.

For example, a student can enter:

```text
Topic: Python
Difficulty: Medium
Questions: 5
```

The AI generates questions related to Python and displays them on the website.

The student can then select answers and immediately see whether the answer is correct or incorrect, along with an explanation.

---

## 2. ❗ Problem Statement

Students often depend on predefined question banks for practicing academic subjects.

Some common problems are:

- Limited number of practice questions
- Repetitive questions
- Difficulty finding questions for specific topics
- No instant AI-generated practice
- Lack of personalized learning
- Manual preparation of quiz questions
- Difficulty adjusting question difficulty

Therefore, an intelligent system is required that can automatically generate study questions based on the student's requirements.

---

## 3. 💡 Proposed Solution

AI Study Partner provides an AI-powered solution for generating educational quizzes.

The system allows the student to:

1. Enter a topic.
2. Select difficulty.
3. Select number of questions.
4. Send the request to the Flask backend.
5. Generate questions using Groq AI.
6. Display the questions in the browser.
7. Select answers.
8. View correct/incorrect results.
9. Read explanations.

---

## 4. 🎯 Objectives

The main objectives of the project are:

- To develop an AI-powered learning assistant.
- To automatically generate quiz questions.
- To provide topic-based learning.
- To provide different difficulty levels.
- To reduce the effort required to prepare practice questions.
- To provide an interactive learning experience.
- To provide instant feedback.
- To demonstrate integration of AI with web development.
- To help students practice academic concepts effectively.

---

## 5. 🚀 Key Features

### 5.1 AI Quiz Generation
The application uses Groq API to generate quiz questions dynamically.

### 5.2 Topic Selection
Students can enter any educational topic, for example:
- Python
- Java
- SQL
- Operating Systems
- Computer Networks
- Data Structures
- DBMS
- HTML
- CSS
- JavaScript

### 5.3 Difficulty Levels
The application supports:
- Easy
- Medium
- Hard

### 5.4 Question Selection
Students can select:
- 5 Questions
- 10 Questions
- 15 Questions

### 5.5 Multiple Choice Questions
Each generated question contains four options.

### 5.6 Instant Feedback
The application highlights:
- Correct answers
- Incorrect answers

### 5.7 Answer Explanation
After answering a question, the application displays an explanation.

### 5.8 Responsive Design
The interface is designed to work on:
- Desktop
- Laptop
- Tablet
- Mobile

### 5.9 Simple User Interface
The system provides a clean and easy-to-use interface suitable for students.

---

## 6. 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| HTML5 | Creates webpage structure |
| CSS3 | Designs and styles the interface |
| JavaScript | Handles user interaction and API communication |
| Python | Backend programming |
| Flask | Web application framework |
| Groq API | AI question generation |
| LLaMA Model | Natural language processing and quiz generation |
| python-dotenv | Loads API key from `.env` |
| Git | Version control |
| GitHub | Source code hosting |
| VS Code | Development environment |

---

## 7. 💻 Hardware Requirements

**Minimum:**
- Processor: Intel Core i3 or equivalent
- RAM: 4 GB minimum
- Storage: 500 MB free space
- Keyboard and mouse
- Internet connection

**Recommended:**
- Processor: Intel Core i5 or equivalent
- RAM: 8 GB or more
- Stable internet connection

---

## 8. 💿 Software Requirements

- Windows / Linux / macOS
- Python 3.x
- Visual Studio Code
- Web Browser
- Git
- Groq API account/API key
- Python Virtual Environment

**Recommended browsers:**
- Google Chrome
- Microsoft Edge
- Mozilla Firefox

---

## 9. 📁 Program Structure

```text
ai-study-partner/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── main.js
```

---

## 10. 📂 Description of Program Files

### `app.py`
The main Python backend program. It is responsible for:
- Starting the Flask server
- Loading the API key
- Connecting to Groq API
- Receiving requests from the frontend
- Sending prompts to the AI
- Processing AI responses
- Returning quiz data to the frontend

### `requirements.txt`
Contains the Python packages required by the project.

```text
Flask
groq
python-dotenv
```

### `.env`
Stores sensitive configuration such as the Groq API key.

```text
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

⚠️ The `.env` file should never be uploaded to GitHub.

### `.gitignore`
Prevents sensitive and unnecessary files from being uploaded to GitHub.

```text
.env
venv/
__pycache__/
*.pyc
```

### `README.md`
Contains complete information about the project, including description, installation, technologies, program structure, architecture, features, testing, and future enhancements.

---

## 11. 🌐 Frontend Structure

```text
templates/
└── index.html

static/
├── css/
│   └── style.css
│
└── js/
    └── main.js
```

### `index.html`
Creates the main user interface. It contains:
- Application title
- Topic input
- Difficulty selection
- Question count selection
- Generate Quiz button
- Loading indicator
- Quiz display area
- Error message area

### `style.css`
Controls the appearance of the application, including:
- Page layout
- Colors
- Fonts
- Buttons
- Input fields
- Quiz cards
- Loading animation
- Responsive design
- Mobile layout

### `main.js`
Controls frontend functionality. It is responsible for:
- Reading user input
- Sending requests to Flask
- Receiving quiz data
- Displaying questions and options
- Checking answers
- Showing correct/incorrect answers
- Displaying explanations
- Handling errors
- Showing loading status

---

## 12. 🏗️ Project Architecture

The system follows a simple client-server architecture.

```text
                    ┌───────────────────┐
                    │      Student      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   Web Interface   │
                    │    HTML/CSS/JS    │
                    └─────────┬─────────┘
                              │
                         HTTP Request
                              │
                              ▼
                    ┌───────────────────┐
                    │   Flask Backend   │
                    │      Python       │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │     Groq API      │
                    │    AI / LLaMA     │
                    └─────────┬─────────┘
                              │
                       Generated Quiz
                              │
                              ▼
                    ┌───────────────────┐
                    │   Flask Backend   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   JavaScript UI   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │      Student      │
                    └───────────────────┘
```

---

## 13. 🧩 System Modules

**Module 1: User Input Module**
The student enters topic, difficulty, and number of questions.

**Module 2: Request Processing Module**
The JavaScript frontend sends the information to the Flask backend.

**Module 3: AI Quiz Generation Module**
The Flask backend sends a prompt to the Groq API, which generates questions based on topic, difficulty, and number of questions.

**Module 4: Response Processing Module**
The Flask backend receives the AI response and processes it into structured quiz data.

**Module 5: Quiz Display Module**
JavaScript displays the generated questions and options.

**Module 6: Answer Evaluation Module**
The selected answer is compared with the correct answer.

**Module 7: Explanation Module**
The application displays an explanation after the student answers.

---

## 14. 🔄 System Workflow

```text
Start
  │
  ▼
Open Application
  │
  ▼
Enter Study Topic
  │
  ▼
Select Difficulty
  │
  ▼
Select Number of Questions
  │
  ▼
Click Generate Quiz
  │
  ▼
JavaScript Sends Request
  │
  ▼
Flask Receives Request
  │
  ▼
Create AI Prompt
  │
  ▼
Send Prompt to Groq API
  │
  ▼
AI Generates Quiz
  │
  ▼
Flask Processes Response
  │
  ▼
Send Quiz to Browser
  │
  ▼
Display Questions
  │
  ▼
Student Selects Answer
  │
  ▼
Check Answer
  │
  ▼
Display Result + Explanation
  │
  ▼
End
```

---

## 15. ⚙️ How the Program Works

**Step 1: Student Opens Website**
The Flask server displays the `index.html` page.

**Step 2: Student Enters Topic** — e.g. `Python`

**Step 3: Student Selects Difficulty** — e.g. `Medium`

**Step 4: Student Selects Questions** — e.g. `5 Questions`

**Step 5: Generate Quiz**
The JavaScript program sends the data to `/generate` using a POST request.

**Step 6: Flask Receives Request**

```text
Topic = Python
Difficulty = Medium
Questions = 5
```

**Step 7: AI Prompt Creation**
Flask creates a prompt for the AI requesting the number of questions, four options, correct answer, explanation, and selected difficulty.

**Step 8: Groq API**
The prompt is sent to the Groq API, which processes the request using an AI language model.

**Step 9: AI Response**
The AI returns structured quiz data:

```json
{
    "questions": [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": [
                "function",
                "def",
                "define",
                "func"
            ],
            "answer": "def",
            "explanation": "The def keyword is used to define a function in Python."
        }
    ]
}
```

**Step 10: Display Quiz**
JavaScript receives the response and creates quiz cards dynamically.

**Step 11: Answer Selection**
The student selects an option.

**Step 12: Answer Evaluation**
The selected answer is compared with the correct answer:
- ✅ Correct Answer
- ❌ Incorrect Answer (the correct answer is also highlighted)

**Step 13: Explanation**
The application displays an explanation for the question.

---

## 16. 🤖 Groq API Integration

Groq API is used as the Artificial Intelligence service in this project. The application uses Groq to generate quiz questions dynamically, accessed from the Python Flask backend.

Basic integration:

```python
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
```

The backend sends a prompt using the Groq client.

---

## 17. 🔐 API Key Management

The API key is stored in the `.env` file:

```text
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

The Python application reads the key using:

```python
os.getenv("GROQ_API_KEY")
```

This prevents the API key from being directly written inside the source code. The `.env` file is excluded from GitHub using `.gitignore`.

---

## 18. 📡 API Endpoint

**`POST /generate`** — generates the AI quiz.

**Request example:**

```json
{
    "topic": "Python",
    "difficulty": "Medium",
    "number_of_questions": 5
}
```

**Response example:**

```json
{
    "questions": [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": [
                "function",
                "def",
                "define",
                "func"
            ],
            "answer": "def",
            "explanation": "The def keyword is used to define a function."
        }
    ]
}
```

---

## 19. 🎨 User Interface

- **Header** — Displays "📚 AI Study Partner"
- **Topic Input** — Allows the student to enter a topic
- **Difficulty Dropdown** — Easy / Medium / Hard
- **Question Count** — 5 / 10 / 15 Questions
- **Generate Button** — Starts AI quiz generation
- **Loading Indicator** — Displays "AI is preparing your quiz..."
- **Quiz Area** — Displays generated questions and answers

---

## 20. ⚙️ Installation

**Step 1: Install Python**

Install Python 3.x on your computer, then check the version:

```bash
python --version
```

**Step 2: Open Project Folder**

Open the project folder in Visual Studio Code.

**Step 3: Create Virtual Environment**

```bash
python -m venv venv
```

**Step 4: Activate Virtual Environment**

For Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

**Step 5: Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## 21. 🔑 Configuration

Create a `.env` file in the main project directory:

```text
ai-study-partner/
│
├── app.py
├── .env
└── requirements.txt
```

Add the following to `.env`:

```text
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Replace the value with your actual Groq API key.

---

## 22. ▶️ Running the Application

Activate the virtual environment:

```bash
.\venv\Scripts\Activate.ps1
```

Run the Flask application:

```bash
python app.py
```

The terminal should display:

```text
Running on http://127.0.0.1:5000
```

Open the browser and visit:

```text
http://127.0.0.1:5000
```

---

## 23. 🧪 Testing

### Functional Testing

| Test | Expected Result |
|---|---|
| Enter topic | Topic accepted |
| Select difficulty | Difficulty selected |
| Select questions | Question count selected |
| Click Generate | Quiz generated |
| Select correct answer | Correct answer highlighted |
| Select wrong answer | Wrong answer highlighted |
| — | Explanation displayed |
| Empty topic | Error displayed |

### API Testing

The Groq API should be tested for:
- Valid API key
- Invalid API key
- Missing API key
- Network errors
- Invalid AI response
- Empty topic

### UI Testing

The interface should be tested on:
- Desktop
- Laptop
- Tablet
- Mobile

---

## 24. ✅ Advantages

- Automatic quiz generation
- Fast AI response
- Easy-to-use interface
- Topic-based learning
- Multiple difficulty levels
- Multiple-choice questions
- Instant feedback
- AI-generated explanations
- Reduces manual question preparation
- Can be extended into a complete learning platform

---

## 25. ⚠️ Limitations

- Requires internet connection
- Requires Groq API access
- AI-generated questions may occasionally contain errors
- Current version does not permanently store student performance
- No user authentication in the basic version
- No database in the basic version
- Quiz history is not permanently saved

---

## 26. 🔮 Future Enhancements

**User Authentication** — Registration, Login, Logout, User profiles

**Database** — Use SQLite, MySQL, or PostgreSQL to store user accounts, quiz history, scores, topics, and performance

**Student Dashboard** — Show total quizzes, total questions, correct/incorrect answers, accuracy, weak topics, and strong topics

**Adaptive Learning** — Automatically adjust question difficulty according to student performance:

```text
High Performance → Harder Questions
Low Performance  → Easier Questions
```

**Notes/PDF Upload** — Students can upload study material:

```text
PDF → AI Reads Content → Extract Important Topics → Generate Quiz
```

**AI Explanations** — Detailed explanations for incorrect answers

**Leaderboard** — Compare scores with other users

**Gamification** — XP, Badges, Levels, Achievements, Daily challenges

**Multi-Language Support** — Support multiple languages for students from different regions

---

## 27. 🎓 Applications

- College students
- School students
- Competitive exam preparation
- Technical interview preparation
- Self-learning
- Online education
- Practice tests
- Revision
- Programming practice

---

## 28. 🔐 Security

**API Key Protection** — API keys are stored in `.env`

**Git Protection** — `.env` is included in `.gitignore`

**Input Validation** — The application checks whether the topic has been entered

**Backend API** — The Groq API key is accessed from the backend rather than exposed directly in JavaScript

---

## 29. 📊 Project Input and Output

**Input:**

```text
Topic: Python
Difficulty: Medium
Questions: 5
```

**Processing:**

```text
User Input → JavaScript → Flask → Prompt Generation → Groq API → AI Model
```

**Output:**
- Question
- Option A, B, C, D
- Correct Answer
- Explanation

---

## 30. 📸 Expected Application Screens

### Home Screen

```text
-----------------------------------------
        📚 AI Study Partner

        Your Personal AI Study Partner

        [ Enter Study Topic ]

        Difficulty: [ Medium ]

        Questions: [ 5 Questions ]

        [ ✨ Generate Quiz ]
-----------------------------------------
```

### Quiz Screen

```text
Question 1

Which keyword is used to define
a function in Python?

A. function
B. def
C. define
D. func
```

After selecting an answer:

```text
✅ Correct Answer

Explanation:
The def keyword is used to define
a function in Python.
```

---

## 31. 📚 Learning Outcomes

Through this project, the developer gains practical knowledge of:

- Python programming
- Flask web development
- HTML, CSS, JavaScript
- REST-style API communication
- AI API integration
- JSON data handling
- Environment variables
- Virtual environments
- Error handling
- Git and GitHub
- Frontend-backend communication
- AI prompt design

---

## 32. 🧠 Concepts Used

**Python:** Variables, Functions, Conditional statements, Exception handling, Modules, Environment variables

**Flask:** Routes, HTTP requests, JSON responses, Templates, Backend processing

**JavaScript:** DOM manipulation, Functions, Events, Fetch API, JSON handling, Dynamic HTML generation, Error handling

**HTML:** Forms, Input fields, Buttons, Containers, Semantic structure

**CSS:** Layout, Flexbox, Grid, Responsive design, Animations, Styling

**Artificial Intelligence:** Prompt engineering, Natural language processing, AI-generated content, AI API integration

---

## 33. 🔗 Frontend and Backend Communication

The frontend communicates with the backend using the Fetch API:

```javascript
fetch("/generate", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        topic: topic,
        difficulty: difficulty,
        number_of_questions: numberOfQuestions
    })
});
```

The Flask backend receives this request and sends it to Groq. The generated result is then returned to JavaScript.

---

## 34. 🗂️ Complete Technology Stack

```text
                 AI STUDY PARTNER
                        │
        ┌───────────────┼───────────────┐
        │               │               │
    Frontend         Backend            AI
        │               │               │
     HTML5            Python          Groq API
     CSS3             Flask           LLaMA
     JavaScript
        │               │               │
        └───────────────┼───────────────┘
                        │
                   Web Browser
```

---

## 35. 📋 Project Summary

| Category | Details |
|---|---|
| Project Name | AI Study Partner |
| Project Type | BCA Academic Project |
| Domain | Artificial Intelligence |
| Sub-Domain | Education Technology |
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| AI API | Groq API |
| AI Model | LLaMA |
| Database | Not included in basic version |
| API Communication | HTTP / JSON |
| Development Tool | Visual Studio Code |
| Version Control | Git |
| Repository | GitHub |
| Platform | Web Application |

---

## 36. 🌟 Project Highlights

- AI-powered educational system
- Dynamic quiz generation
- Groq API integration
- Python Flask backend
- Interactive JavaScript frontend
- Multiple difficulty levels
- Automatic answer checking
- AI-generated explanations
- Responsive user interface
- Secure API key handling

---

## 37. 🚀 Future Vision

The long-term goal of AI Study Partner is to become a complete personalized AI learning platform:

```text
Student
   │
   ▼
Upload Notes
   │
   ▼
AI Understands Study Material
   │
   ▼
Identify Important Topics
   │
   ▼
Generate Personalized Quiz
   │
   ▼
Student Attempts Quiz
   │
   ▼
Analyze Performance
   │
   ▼
Identify Weak Areas
   │
   ▼
Recommend Next Topics
   │
   ▼
Personalized Learning
```

---

## 38. 🏁 Conclusion

AI Study Partner is an AI-powered web application that demonstrates how Artificial Intelligence can be integrated with modern web technologies to improve the learning experience.

The system allows students to enter a topic and generate customized quizzes using Groq AI. Flask provides the backend, while HTML, CSS, and JavaScript provide the frontend interface.

The application demonstrates important concepts such as AI API integration, frontend-backend communication, JSON processing, prompt engineering, error handling, and responsive web design.

Although the current version provides basic quiz generation and answer evaluation, it can be expanded with user accounts, databases, performance analytics, adaptive learning, PDF processing, leaderboards, gamification, and personalized recommendations.

Therefore, AI Study Partner provides a strong foundation for developing a complete AI-based educational platform.

---

## 39. 👨‍💻 Developer

- **Name:** Mith
- **Degree:** Bachelor of Computer Applications (BCA)
- **Project:** AI Study Partner
- **Project Type:** Academic / Final Year Project

---

## 40. 📄 License

This project is developed for educational and academic purposes.

---

### ⭐ Final Statement

**AI Study Partner** combines:

```text
Python + Flask + HTML + CSS + JavaScript + Groq API + AI Language Model = AI Study Partner
```

It demonstrates the practical use of Artificial Intelligence in education and provides a foundation for future development into a personalized AI learning platform.