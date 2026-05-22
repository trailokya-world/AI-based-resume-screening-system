from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor
import spacy
from spacy.matcher import PhraseMatcher
import re


nlp = spacy.load("en_core_web_lg")
skill_extractor_model = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)


CUSTOM_SKILLS = [
    # Programming languages
    "python", "java", "c++", "c#", "r", "scala", "javascript",
    "typescript", "golang", "rust", "kotlin", "swift", "php", "ruby",

    # ML / AI
    "machine learning", "deep learning", "nlp", "natural language processing",
    "computer vision", "reinforcement learning", "transfer learning",
    "neural network", "transformer", "bert", "gpt", "llm",
    "generative ai", "large language model",

    # Frameworks & libraries
    "tensorflow", "pytorch", "keras", "scikit-learn", "xgboost",
    "lightgbm", "huggingface", "spacy", "nltk", "opencv",
    "pandas", "numpy", "matplotlib", "seaborn", "plotly",

    # Data & databases
    "sql", "mysql", "postgresql", "mongodb", "redis", "elasticsearch",
    "cassandra", "sqlite", "oracle", "firebase", "bigquery",

    # Cloud & DevOps
    "aws", "azure", "gcp", "google cloud", "docker", "kubernetes",
    "ci/cd", "jenkins", "github actions", "terraform", "ansible",

    # Data tools
    "power bi", "tableau", "excel", "spark", "hadoop", "airflow",
    "dbt", "kafka", "etl", "data pipeline", "data warehouse",

    # Web
    "rest api", "fastapi", "flask", "django", "react", "node.js",
    "html", "css",

    # Other
    "git", "linux", "agile", "scrum", "statistics", "data analysis",
    "data visualization", "feature engineering", "model deployment",
    "mlops", "a/b testing", "time series"
]


def skillner_extract(text):
    """Extract skills using skillNer"""
    try:
        annotations = skill_extractor_model.annotate(text)

        full_matches = [
            s["doc_node_value"].lower().strip()
            for s in annotations["results"]["full_matches"]
        ]
        ngram_matches = [
            s["doc_node_value"].lower().strip()
            for s in annotations["results"]["ngram_scored"]
            if s["score"] >= 0.7          # ✅ filter low confidence matches
        ]
        return set(full_matches + ngram_matches)

    except Exception as e:
        print(f"skillNer error: {e}")
        return set()


def custom_skill_extract(text):
    """Extract skills using custom keyword matching with PhraseMatcher"""
    matcher  = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp.make_doc(skill) for skill in CUSTOM_SKILLS]
    matcher.add("CUSTOM_SKILLS", patterns)

    doc     = nlp(text.lower())
    matches = matcher(doc)

    found = set()
    for match_id, start, end in matches:
        found.add(doc[start:end].text.lower().strip())

    return found


def regex_skill_extract(text):
    """Catch skills written in special formats skillNer misses"""
    text_lower = text.lower()
    found      = set()


    special_skills = {
        "c\+\+"         : "c++",
        "c#"            : "c#",
        "\.net"         : ".net",
        "node\.js"      : "node.js",
        "scikit\-learn" : "scikit-learn",
        "ci/cd"         : "ci/cd",
        "power\s*bi"    : "power bi",
        "ms\s*excel"    : "excel",
        "rest\s*api"    : "rest api",
        r"\bml\b"       : "machine learning",
        r"\bnlp\b"      : "nlp",
        r"\bai\b"       : "artificial intelligence",
        r"\baws\b"      : "aws",
        r"\bgcp\b"      : "gcp",
        r"\bsql\b"      : "sql",
        r"\bapi\b"      : "api",
    }

    for pattern, skill_name in special_skills.items():
        if re.search(pattern, text_lower):
            found.add(skill_name)

    return found


def skill_extractor(raw_text):
    """
    Combined skill extractor:
    skillNer + custom PhraseMatcher + regex
    for maximum coverage and accuracy
    """

  
    skillner_skills = skillner_extract(raw_text)
    custom_skills   = custom_skill_extract(raw_text)
    regex_skills    = regex_skill_extract(raw_text)

   
    all_skills = skillner_skills | custom_skills | regex_skills

   
    filtered_skills = {
        skill for skill in all_skills
        if len(skill) >= 2                          
        and skill not in {"the", "and", "for",
                          "use", "with", "using"}   
    }


    return sorted(filtered_skills)