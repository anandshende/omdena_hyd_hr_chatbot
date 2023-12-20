import nltk
nltk.download('punkt')  # Download the punkt tokenizer data

def split_into_sentences(paragraph):
    sentences = nltk.sent_tokenize(paragraph)
    return sentences
