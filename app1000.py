import streamlit as st
from resume_parser import ResumeParser

pdf = "CV (Manisha jain) doc-converted.pdf"
data = ResumeParser(pdf).get_extracted_data()
st.write(data)
