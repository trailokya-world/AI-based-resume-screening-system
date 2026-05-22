import nltk
import re
from nltk import WordNetLemmatizer


def preprocessing(input):
    
    stop_words = nltk.corpus.stopwords.words("english")
    lemmatizer = WordNetLemmatizer()
    
    if type(input) != str:
        resume_dict = {}
        for name, resume in input.items():

            text = resume.lower()
            text = re.sub(r'[^a-zA-Z\s]', '', text)
            text = " ".join(word for word in text.split() if word not in stop_words)
            text = " ".join(lemmatizer.lemmatize(word) for word in text.split())
            
            resume_dict[name] = text
        
        return resume_dict  
    else:
        text = input.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = " ".join(word for word in text.split() if word not in stop_words)
        text = " ".join(lemmatizer.lemmatize(word) for word in text.split())

        return text