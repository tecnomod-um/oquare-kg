import pandas as pd
from pathlib import Path
import argparse


# Define the dictionary characteristic → List of characteristics
subcharacteristics = {
    "Formalisation": [
        "Used vocabularies metric"
    ],
    "Structural accuracy": [
        "Deprecated terms metric",
        "Misused properties metric",
        "Misplaced class property metric"
    ],
    "Consistency": [
        "Misused properties metric",
        "Misplaced class property metric",
        "Compatible datatype metric",
        "Classes per instance metric",
        "Instances with multiple types metric",
        "Usage of undefined terms metric",
        "Entities with no type metric"
    ],
    "Syntactic validity": [
        "Compatible datatype metric",
        "Different serialisation formats metric",
        "Valid format metric"
    ],
    "Redundancy": [
        "Extensional conciseness metric"
    ],
    "Interpretability": [
        "Entities with no type metric",
        "Reuse terms metric",
        "Usage of undefined terms metric",
        "Classes per instance metric",
        "Instances with multiple types metric"
    ],
    "Inference": [
        "Used vocabularies metric",
        "Entities with no type metric",
        "Usage of undefined terms metric",
        "Classes per instance metric",
        "Instances with multiple types metric"
    ],
    "Understandability": [
        "Instances with no description metric",
        "Instances with no name metric",
        "Instances with no synonyms metric",
        "Descriptions per instance metric",
        "Names per instance metric",
        "Synonyms per instance metric",
        "Annotation richness metric",
        "Used vocabularies metric"
    ],
    "Trustworthiness": [
        "Evidence metric",
        "Traceability of the data metric"
    ],
    "Provenance": [
        "Basic provenance metric",
        "Traceability of the data metric"
    ],
    "Clustering": [
        "Entities with no type metric",
        "Relations per node metric",
        "Synonyms per instance metric",
        "Usage of undefined terms metric",
        "Classes per instance metric",
        "Instances with multiple types metric"
    ],
    "Interoperability": [
        "Reuse terms metric",
        "Used vocabularies metric",
        "Different serialisation formats metric",
        "Valid format metric"
    ],
    "Versatility": [
        "Different serialisation formats metric",
        "Multiple languages metric"
    ],
    "Licensing": [
        "Machine license metric",
        "Human readable license metric"
    ],
    "Accessibility": [
        "Dereferenceable uris metric",
        "Basic provenance metric",
        "Traceability of the data metric",
        "Different serialisation formats metric"
    ],
    "Reusability": [
        "Reuse terms metric",
        "Machine license metric",
        "Human readable license metric",
        "Used vocabularies metric",
        "Basic provenance metric",
        "Traceability of the data metric"
    ]
}


# Read the CSV with metrics per graph

parser = argparse.ArgumentParser(description="Calculate subcharacteristics")

parser.add_argument("--input", type=Path, required=True)
parser.add_argument("--output", type=Path, required=True)

args = parser.parse_args()

input_path = args.input
output_path = args.output

df = pd.read_csv(input_path)
# print(df.columns.tolist())


# Create a new table: rows = graphs, columns = subcharacteristics
result_table = pd.DataFrame()
result_table["graph"] = df["graph"]

# For each subcharacteristic, sum or average the associated metrics
for subchar, metric_list in subcharacteristics.items(): 
    result_table[subchar] = df[metric_list].mean(axis=1)


# Save the result table to a CSV file
result_table.to_csv(output_path, index=False)
print(f"Save in: {output_path}")
print("CSV file with subcharacteristics calculated successfully.")