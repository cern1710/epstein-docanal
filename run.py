from src import markov, parser

doc_path = "doc.pdf"

if __name__ == "__main__":
    parser.extract_text(doc_path)
    model = markov.HiddenMarkovModel