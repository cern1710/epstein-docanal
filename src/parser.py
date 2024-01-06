'''
Uncomment these lines if you haven't downloaded punkt already!
'''
# import nltk
# nltk.download('punkt')

from pypdf import PdfReader
import re
from nltk.tokenize import word_tokenize

def parse_doc(pdf_path):
    reader = PdfReader(pdf_path)
    all_text = ""
    for page in reader.pages:
        all_text += page.extract_text() + '\n'
    return all_text

def clean_doc(lines):
    cleaned_text = []
    for line in lines:
        line = line.lower()
        line = re.sub(r"[,.\"\'!@#$%^&*(){}?/;`~:<>+=-\\]", "", line)
        tokens = word_tokenize(line)
        cleaned_text += [word for word in tokens if word.isalpha()]
    return cleaned_text

def extract_text(pdf_path):
    text = parse_doc(pdf_path)
    cleaned_text = clean_doc(text)
    return cleaned_text