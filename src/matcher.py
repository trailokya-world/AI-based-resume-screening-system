import pandas as pd
from src.vectorizers import cosine_score
from  src.skill_extractor import skill_extractor

def output_generator(resume_dict, job_description):
    scores = []
    names = [] 
    skills = []
    
    for value in resume_dict.values():
        score = cosine_score(value, job_description)*100
        scores.append(score.round(2))
    
     
    for key in resume_dict.keys():
        names.append(key)

    for value in resume_dict.values():
        
        all_skills = skill_extractor(value)
        skills.append(all_skills)
        
    final_output = pd.DataFrame({"Names":names,
                                 "Scores":scores,
                                 "Skills":skills})
    
    

    return final_output
