# 🤖 AI-Based Resume Screening System

An intelligent resume screening system that automatically screens resumes against a job description using NLP and machine learning. Upload multiple resumes, paste a job description, and get a **ranked list of candidates** with match scores — all through a clean **Streamlit UI**.

---

## 📌 Features

- 📄 Upload multiple PDF resumes at once
- 📝 Paste any job description to screen against
- 🧹 Preprocesses and cleans resume text using `nltk` and lemmatization
- 🔍 Extracts skills using `skillNer` and `spaCy`
- 🧠 Generates semantic embeddings using `SentenceTransformer` (`BAAI/bge-base-en-v1.5`)
- 📊 Computes cosine similarity score between each resume and the job description
- 🏆 Displays a **ranked list of candidates** by match score
- 🖥️ Interactive **Streamlit** web interface — no coding required

---

## 🖥️ App Preview

> Upload resumes → Paste job description → Click Screen → Get ranked results instantly

---

## 🗂️ Project Structure

```
AI_Resume_Screening/
│
├── data/
│   ├── resumes/                  # Input PDF resumes
│   └── job_descriptions/         # Job description text files
│
├── models/
│   └── embedding_model/          # Saved SentenceTransformer model
│
├── src/
│   ├── parser.py                 # PDF text extraction (pdfplumber)
│   ├── preprocess.py             # Text cleaning & lemmatization (nltk)
│   ├── vectorizer.py             # Semantic embeddings (SentenceTransformer)
│   ├── matcher.py                # Cosine similarity scoring (sklearn)
│   ├── ranker.py                 # Ranks candidates by match score
│   └── skill_extractor.py        # Skill extraction (skillNer + spaCy)
│
├── utils/
│   └── helpers.py                # Shared utility functions
│
├── app.py                        # Streamlit UI entry point
├── requirements.txt              # Project dependencies
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/AI_Resume_Screening.git
cd AI_Resume_Screening
```

### 2. Create and activate a virtual environment
```bash
# Using conda
conda create -n resume_ai_env python=3.11
conda activate resume_ai_env

# Or using venv
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download required models
```bash
# Download NLTK data
python -m nltk.downloader wordnet omw-1.4

# Download spaCy English model
python -m spacy download en_core_web_lg
```

> The `BAAI/bge-base-en-v1.5` SentenceTransformer model will be downloaded automatically on first run (~450MB).

---

## 📦 Requirements

```
pdfplumber
nltk
joblib
sentence-transformers
scikit-learn
spacy
numpy
pandas
skillNer
streamlit
pydantic>=2.0
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`

---

## 🧠 How It Works

```
User Uploads PDFs + Job Description (Streamlit UI)
     │
     ▼
Text Extraction (pdfplumber)
     │
     ▼
Text Preprocessing (nltk, lemmatization, regex)
     │
     ▼
Skill Extraction (skillNer + spaCy)
     │
     ▼
Semantic Embedding (SentenceTransformer - BAAI/bge-base-en-v1.5)
     │
     ▼
Cosine Similarity Score vs Job Description Embedding
     │
     ▼
Ranked List of Candidates (Streamlit UI)
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Streamlit` | Web UI |
| `pdfplumber` | PDF text extraction |
| `nltk` | Text preprocessing & lemmatization |
| `spaCy` | NLP pipeline |
| `skillNer` | Skill extraction from text |
| `SentenceTransformer` | Semantic embeddings |
| `scikit-learn` | Cosine similarity |
| `pandas` / `numpy` | Data handling |
| `joblib` | Model persistence |

---

## 📝 Notes

- Python version **3.9 or above** required
- Pydantic version must be **>=2.0** (`pip install pydantic --upgrade`)
- First run downloads the embedding model (~450MB) — internet connection required

---

## 👤 Author

**Trailokya**
Data Science | AI/ML Projects
📍 Kolhapur, Maharashtra, India

---





