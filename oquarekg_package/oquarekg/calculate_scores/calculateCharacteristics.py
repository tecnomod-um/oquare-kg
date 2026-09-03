import pandas as pd
from pathlib import Path
import argparse


# Define the dictionary characteristic → List of characteristics
characteristics = {
    "Structural": [
        "Formalisation",
        "Structural accuracy",
        "Consistency",
        "Syntactic validity",
        "Redundancy",
        "Interpretability",
    ],
    "Functional adequacy": [
        "Inference",
        "Understandability",
        "Trustworthiness",
        "Provenance",
        "Clustering",
    ],
    "Compatibility": [
        "Interoperability",
    ],
    "Transferability": [
        "Versatility",
    ],
    "Operability": [
        "Licensing",
    ],
    "Reliability": [
        "Accessibility",
    ],
    "Maintainability": [
        "Reusability",
    ],
}


# Read the CSV with metrics per graph
parser = argparse.ArgumentParser(description="Calculate characteristics")

parser.add_argument("--input", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)

args = parser.parse_args()

input_path = args.input
output_path = args.output

df = pd.read_csv(input_path)
# print("COLUMNAS:")
# print(df.columns.tolist())
# print(df.head())


# Create a new table: rows = graphs, columns = characteristics
result_table = pd.DataFrame()
result_table["graph"] = df["graph"]

for subchar, subchar_list in characteristics.items(): # For each subcharacteristic, sum or average the associated metrics
    result_table[subchar] = df[subchar_list].mean(axis=1)


# Save the result table to a CSV file
result_table.to_csv(output_path, index=False)
print(f"Save in: {output_path}")
print("CSV file with characteristics calculated successfully.")