import resume_parser
import streamlit as st
import nltk
import spacy
nlp = spacy.load("en_core_web_sm")
myresume="CV (Manisha jain) doc-converted.pdf"
data = resume_parser.ResumeParser(myresume).get_extracted_data()
st.write(data)
