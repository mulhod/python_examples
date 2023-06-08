import nltk
import numpy as np

nltk.download("punkt")


def extract_features(text):
    features = {}
    text = text.strip()
    features["length##" + str(int(np.log2(len(text) + 1)))] = 1
    tokens = nltk.tokenize.word_tokenize(text)
    text = text.lower()
    for n in range(2, 6):
        for i in range(len(text)):
            c_ngram = text[i:i + n]
            if len(c_ngram) != n:
                break
            features["cngram##" + c_ngram] = 1
    for n in range(1, 6):
        for i in range(len(tokens)):
            w_ngram = tokens[i:i + n]
            if len(w_ngram) != n:
                break
            features["wngram##" + " ".join(w_ngram).lower()] = 1
    return features


if __name__ == "__main__":
    print(extract_features("Hello, class!"))
