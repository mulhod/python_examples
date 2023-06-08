import json

import pandas as pd

from feature_extractor import extract_features


def main():

   df = pd.read_csv("Fruitfly.tsv", sep="\t")
   features = [extract_features(text) for text in df["text"]]
   print(json.dumps(features[:5], indent=4))


if __name__ == "__main__":
    main()
