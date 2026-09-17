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
