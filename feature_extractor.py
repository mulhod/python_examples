def extract_features(text):
    features = {}
    features["clength"] = len(text)
    tokens = nltk.tokenize.word_tokenize(text)
    features["tlength"] = len(tokens)
    for c in text:
        features["c##" + c] = 1
    for i in range(len(text)):
        c_bigram = text[i:i + 2]
        if len(c_bigram) !=2:
            break
        features["c##" + c_bigram] = 1
    for token in tokens:
        features["t##" + token] = 1
    for i in range(len(tokens)):
        w_bigram = tokens[i:i + 2]
        if len(w_bigram) != 2:
            break
        features["t##" + " ".join(w_bigram)] = 1
    return features
