import nltk
from nltk.tokenize import sent_tokenize

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")


def segment_text(text):

    sentences = sent_tokenize(text)

    if len(sentences) < 3:
        sentences = text.split(".")

    return [s.strip() for s in sentences if s.strip()]