# Name: Xuanyi Jin
# ID: 30804299
# Start Date: 19 Sep 2019
# Last Modified: 20 Sep 2019
import os
from time import time

from idf_30804299 import IDFAnalyser
from preprocessor_30804299 import Preprocessor
from word_30804299 import WordAnalyser


# Load txt files in current working directory.
#     Returns:
#         list
#             list of filenames
def load_documents():
    documents = []
    # get the current working directory
    path = os.getcwd()
    # walk through current working directory, grab documents
    for root, directory, files in os.walk(path, topdown=False):
        for file in files:
            if file.endswith(".txt") and not root.endswith("test_data"):
                documents.append(file)
    return documents


# Uses Term Frequency-Inverse Document Frequency (TF-IDF) to determine
# the most suitable document for a given term.
#     Parameters:
#         term: str
#             a string indicating what term is being used to search
#         documents: list
#             documents to be chose from
#     Returns:
#         str
#             the name of the document that returns the highest TF-IDF amongst all documents
def choice(term, documents):
    # Lower the term
    term_lower = term.lower()
    # Initialize processors and analysers.
    preprocessor = Preprocessor()
    word_analyser = WordAnalyser()
    idf_analyser = IDFAnalyser()

    # 1. Preprocess documents.
    # Store the documents in a dict{document_name: document_content}
    cleaned_documents = {}
    for document in documents:
        preprocessor.read_text(document)
        preprocessor.clean()
        cleaned_documents[document[:-4]] = preprocessor.book_content

    # 2. Analyze cleaned documents and get TFs.
    # Store tfs in a dict{document_name: tf}
    term_frequencies = {}
    for document, book_text in cleaned_documents.items():
        word_analyser.analyse_words(book_text)
        term_frequencies[document] = word_analyser.get_word_frequency()

    # 3. Calculate IDF of term.
    #                           value: term frequencies          key: book(document) titles
    idf_analyser.load_frequency(list(term_frequencies.values()), list(term_frequencies.keys()))
    idf = idf_analyser.get_IDF(term_lower)

    # 4. Calculate tf-idfs of each document, TF-IDF = tf(term, document) * idf(term, documents)
    #    and find the document with highest tf-idf.
    tf_idfs = dict([(document, tf[term_lower] * idf) for document, tf in term_frequencies.items() if term_lower in tf])
    highest_score = None
    highest_document = None
    for document, tf_idf in tf_idfs.items():
        if highest_score is not None and tf_idf < highest_score:
            continue
        highest_score = tf_idf
        highest_document = document

    return highest_document


if __name__ == "__main__":
    required_term = "Wollstonecraft"
    docs = load_documents()
    query_result = choice(required_term, docs)
    print("Recommended book: " + str(query_result))
