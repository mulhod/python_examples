import joblib
import os
import json
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from sklearn.metrics import cohen_kappa_score
from sklearn.svm import SVR
from sklearn.feature_extraction import DictVectorizer

from firstmodel.feature_extractor import extract_features


def predict(text, model, vec):
    features = extract_features(text)
    features = vec.transform([features])
    return model.predict(features)[0]



def main():

    parser = ArgumentParser(
        description="Runs a ML train/eval experiment.",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--input_file_name", "-i",
        help="Input file name.",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--train_sample_size",
        type=float,
        default=0.8,
    )
    parser.add_argument(
        "--output_dir", "-o",
        help="Output directory name.",
        type=str,
        required=True,
    )
    args = parser.parse_args()

    if os.path.exists(args.output_dir):
        raise RuntimeError(
            f"{args.output_dir} already exists! Please remove it or use a "
            "different output directory."
        )
    os.makedirs(args.output_dir)

    if args.input_file_name.endswith(".tsv"):
        sep = "\t"
    elif args.input_file_name.endswith(".csv"):
        sep = ","
    else:
        raise ValueError(
            f"Need a file ending with .tsv or .csv! Got: {args.input_file_name}"
        )
    df = pd.read_csv(args.input_file_name, sep=sep)

    # Shuffling data
    df = df.sample(frac=1.0, random_state=1)

    # Creating train/test sets
    df_train = df.sample(frac=args.train_sample_size, random_state=1)
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

    # Save the model
    joblib.dump(vec, open(os.path.join(args.output_dir, "vectorizer"), "wb"))
    joblib.dump(model, open(os.path.join(args.output_dir, "model"), "wb"))

    # Evaluate model on test set
    with open(os.path.join(args.output_dir, "report.txt"), "w") as report_file:
        print("Pearson's r: " + str(pearsonr(model.predict(X_test), y_test)), file=report_file)
        print(
            "Quadratic weighted kappa: " +
            str(cohen_kappa_score(np.rint(model.predict(X_test)), y_test, weights="quadratic")),
            file=report_file,
        )


if __name__ == "__main__":
    main()
