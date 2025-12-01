import re
import os
from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_resume(file_path):
    if file_path.endswith('.pdf'):
        return extract_pdf_text(file_path)
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    return ""

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return text.strip()

def extract_info(text):
    info = {}
    phone_match = re.search(r'\+?\d[\d\s\-]{8,}\d', text)
    info['phone'] = phone_match.group() if phone_match else None

    skills_list = ['python', 'java', 'sql', 'html', 'css', 'excel', 'django', 'flask', 'javascript']
    info['skills'] = [skill for skill in skills_list if skill in text]

    return info

def tokenize(text):
    doc = nlp(text.lower())
    return [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
