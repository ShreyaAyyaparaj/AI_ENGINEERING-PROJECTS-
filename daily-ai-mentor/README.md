# 🤖 Daily AI Mentor

An AI-powered personal learning automation that generates a structured AI Engineering lesson every day, converts it into a PDF, and delivers it directly via email.

This project was built as a practical AI Engineering learning project, covering LLM APIs, prompt engineering, structured outputs, Pydantic validation, document generation, and automation.

---

## 🚀 Features

- Generate daily AI Engineering lessons using Gemini
- Structured LLM responses using JSON schemas
- Validate AI-generated data using Pydantic
- Save lessons as structured JSON
- Generate professional PDF lessons
- Automatically email the generated PDF
- Secure API credentials using environment variables
- Modular Python project architecture

---

## 🏗️ Architecture

```text



                    Daily AI Mentor
                           │
                           ▼
                    Learning Topic
                           │
                           ▼
                    Prompt Template
                           │
                           ▼
                      Gemini API
                           │
                           ▼
                 Structured JSON Output
                           │
                           ▼
                    Pydantic Validation
                           │
                    ┌──────┴──────┐
                    ▼             ▼
                  JSON           PDF
                                  │
                                  ▼
                               Email

```






##
🧠 AI Engineering Concepts

This project explores:

LLM APIs
Prompt Engineering
Tokens & Tokenization
Embeddings
Vector Similarity
Structured Outputs
JSON Schema
Pydantic
Temperature and generation parameters
Environment Variables
LLM application architecture
Automation
🛠️ Tech Stack
Python
Google Gemini API
Google GenAI SDK
Pydantic
ReportLab
python-dotenv
SMTP / Gmail
📁 Project Structure
daily-ai-mentor/
│
├── app/
│   ├── schemas/
│   │   └── lesson.py
│   ├── llm.py
│   ├── prompts.py
│   ├── storage.py
│   ├── pdf.py
│   ├── emailer.py
│   └── main.py
│
├── experiments/
│   ├── day-02/
│   ├── day-03/
│   ├── day-04/
│   └── day-05/
│
├── output/
├── .gitignore
├── requirements.txt
└── README.md
⚙️ Setup
1. Clone the repository
git clone <your-repository-url>
cd daily-ai-mentor
2. Create a virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key

GMAIL_SENDER=your_email@gmail.com
GMAIL_APP_PASSWORD=your_gmail_app_password
GMAIL_RECEIVER=your_email@gmail.com

Never commit .env to GitHub.

▶️ Run the Application

Navigate to the application directory:

cd app

Run:

python main.py

The application will:

Generate the lesson using Gemini
Validate the response with Pydantic
Generate a PDF
Save the lesson output
Send the PDF through email
🔐 Security

API keys and email credentials are stored using environment variables.

Sensitive files such as .env are excluded using .gitignore.

📌 Current Status
Project 1 — MVP Complete ✅

Implemented:

 Gemini API integration
 Prompt engineering
 Structured outputs
 Pydantic validation
 JSON storage
 PDF generation
 Email delivery
Upcoming
 Automatic daily execution
 Dynamic learning roadmap
 Progress tracking
 RAG-based learning assistant
 Vector database integration
 Agentic workflows