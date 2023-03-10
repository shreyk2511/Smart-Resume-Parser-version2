#import streamlit as st
#from resume_parser import ResumeParser

#pdf = "C:\\Users\\shrey\\pythonProject\\CV (Manisha jain) doc-converted.pdf"
#data = ResumeParser(pdf).get_extracted_data()
#st.write(data)

from pyresparser import ResumeParser
pdf = "C:\\Users\\shrey\\pythonProject\\CV (Manisha jain) doc-converted.pdf"
data = ResumeParser(pdf).get_extracted_data()
print(data)