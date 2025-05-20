# LLM Resume Screener

A simple AI-powered resume analysis tool using FastAPI and OpenAI.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Add your OpenAI API key to `.env`

3. Run the API:

```bash
uvicorn main:app --reload
```

## Endpoint

POST `/analyze/`

- `file`: Resume file (.pdf)
- `job_description`: Job description as text
