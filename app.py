from src.parser import pdf_reader2
from src.preprocess import preprocessing
from src.matcher import output_generator
from src.parser import pdf_reader2
from src.ranker import ranker
import streamlit as st

resumes = st.file_uploader("enter resume:",type=["pdf"], accept_multiple_files=True)
st.write(f"{len(resumes)} Files Added Successfully")
raw_job_description = st.text_area("Enter Job Description",height=200)
job_description = preprocessing(raw_job_description)

clicked = st.button("Processe")

if clicked:

    if resumes and job_description:
        
        # parsing
        with st.spinner("Reading and Processing Resumes..."):
           raw_resume_dict = pdf_reader2(resumes)
        st.success(f"{len(raw_resume_dict)} Resumes Scanned Successfully")
          
        # preprocessing
        with st.spinner("Reading and Processing resumes..."):
            resume_dict = preprocessing(raw_resume_dict)   
        st.success(f"{len(resume_dict)} Resumes Processed Successfully")  
        
        # vectorizer, matcher, skills extractor
        with st.spinner("Matching..."):
            final_output = output_generator(resume_dict,job_description)
        st.success("Matched Successfully")
         
        # ranking    
        with st.spinner("Ranking..."):
            ranked_output = ranker(final_output)
        st.success("Ranked Successfully")    
            
        st.subheader("Result")
        st.dataframe(ranked_output)

    elif resumes and not job_description:
        st.write("Please Enter Job Description")
        
    else:
        st.write("Please add Resumes")






