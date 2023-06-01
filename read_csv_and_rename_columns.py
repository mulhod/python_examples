from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

import pandas as pd


def main():
    parser = ArgumentParser(
        description="Reads in file and renames columns to proudce new file.",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--input_file_name", "-i",
        help="Input file name.",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--output_file_name", "-o",
        help="Output file name.",
        type=str,
        required=True,
    )
    args = parser.parse_args()

    df = pd.read_csv(args.input_file_name)
    df.rename(
        columns={
            "Student ID": "id", "Human Score #1": "score", "Student Text Response": "text"
        },
        inplace=True
    )
    df.to_csv(args.output_file_name, index=False)


if __name__ == "__main__":
    main()
