import os
import pdfplumber

def pdf_reader2(uploaded_files):
    
    raw_resume_dict = {}
    for uploaded_file in uploaded_files:
        
        # full_path = os.path.join(path)

        with pdfplumber.open(uploaded_file) as pdf:
            text = " "
            for page in pdf.pages:
                extracted= page.extract_text()
                if extracted:
                    text +=extracted + " "
                
        raw_resume_dict[uploaded_file.name] = text
                  
    return raw_resume_dict