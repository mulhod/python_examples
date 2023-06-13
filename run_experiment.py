import json

import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from sklearn.metrics import cohen_kappa_score
from sklearn.svm import SVR
from sklearn.feature_extraction import DictVectorizer

from feature_extractor import extract_features


def main():

    df = pd.read_csv("Fruitfly.tsv", sep="\t")

    # Shuffling data
    df = df.sample(frac=1.0, random_state=1)

    # Creating train/test sets
    df_train = df.sample(frac=0.8, random_state=1)
    df_test = df[~df["id"].isin(df_train["id"])]

    # Extract features and scores
    vec = DictVectorizer()
    X_train = df_train["text"].apply(extract_features).values
    X_train = vec.fit_transform(X_train)
    y_train = df_train["score"].values
    X_test = df_test["text"].apply(extract_features).values
    X_test = vec.transform(X_test)
    y_test = df_test["score"].values

    # Train model
    model = SVR(gamma="scale", C=0.01, kernel="linear")
    model.fit(X_train, y_train)

    # Evaluate model on test set
    print("Pearson's r: " + str(pearsonr(model.predict(X_test), y_test)))
    print(
        "Quadratic weighted kappa: " +
        str(cohen_kappa_score(np.rint(model.predict(X_test)), y_test, weights="quadratic"))
    )


if __name__ == "__main__":
    main()
