import pandas as pd


def main():
    file_name = "test.csv"
    df = pd.read_csv(file_name)
    print(df)


if __name__ == "__main__":
    main()

