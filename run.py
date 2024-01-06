from src import markov, parser
import os

doc_path = "docs/doc.pdf"
extracted_path = "docs/extracted_text.txt"
check_path = "docs/check.txt"

if __name__ == "__main__":
    if os.path.exists(extracted_path):
        corpus = parser.read_extracted_doc(extracted_path)
        print(corpus)
    else:
        corpus = parser.extract_text(doc_path)
        file = open(extracted_path, 'w+')
        for word in corpus:
            file.write(word + ' ')
        file.close()