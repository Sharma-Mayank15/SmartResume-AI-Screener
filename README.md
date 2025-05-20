
# SmartResume-AI-Screener

**SmartResume-AI-Screener** is an AI-powered resume screening system that helps recruiters automatically analyze and shortlist candidate resumes using Natural Language Processing (NLP) and Machine Learning techniques.

---

## Features

- Extracts key information from resumes (education, skills, experience).
- Uses AI models to score and rank candidates.
- Supports multiple resume formats (PDF, DOCX).
- Easy to deploy and extend.

---

## Getting Started

### Prerequisites

- Python 3.10 or above
- Git
- [Optional] Virtual environment tool (recommended: `venv` or `conda`)

---

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Sharma-Mayank15/SmartResume-AI-Screener.git
cd SmartResume-AI-Screener
```

2. **Create and activate a virtual environment (recommended)**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file in the project root and add your OpenAI API key and any other secrets here:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

### Usage

Run the main application to start screening resumes:

```bash
python main.py
```

Follow any on-screen prompts to upload resumes or configure screening parameters.

---

## Important Notes

- **Security:** Never commit `.env` files or secret keys to the repository.
- **Cache files:** Python cache files (`__pycache__`) are excluded from the repo.
- **Push protection:** Your repo uses GitHub Push Protection to prevent committing secrets.




---

## License

This project is licensed under the MIT License.
