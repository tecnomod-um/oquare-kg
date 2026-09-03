from pathlib import Path
import csv
import argparse


# Arguments
parser = argparse.ArgumentParser(description="Global normalisation + Likert (per file output)")
parser.add_argument("--input_dir", type=Path, required=True)
parser.add_argument("--outdir", type=Path, required=True)

args = parser.parse_args()

input_dir = args.input_dir
outdir = args.outdir
outdir.mkdir(exist_ok=True)

# Metrics mapping
mapping_direct = {
    "Basic provenance metric",
    "Compatible datatype metric",
    "Dereferenceable uris metric",
    "Multiple languages metric",
    "Reuse terms metric",
    "Traceability of the data metric",
    "Used vocabularies metric",
}

mapping_inverse = {
    "Deprecated terms metric",
    "Entities with no type metric",
    "Extensional conciseness metric",
    "Instances with no description metric",
    "Instances with no name metric",
    "Instances with no synonyms metric",
    "Misplaced class property metric",
    "Misused properties metric",
    "Usage of undefined terms metric",
}

mapping_boolean_metrics = {
    "Human readable license metric",
    "Machine license metric",
    "Valid format metric",
}

# Metrics that are normalized from 0 to infinity
mapping_zero_to_infinity = {
    "Annotation richness metric",
    "Classes per instance metric",
    "Relations per node metric",
    "Names per instance metric",
    "Descriptions per instance metric",
    "Synonyms per instance metric",
    "Evidence metric",
}

# Direct mapping for specific metrics
metric_serialization = "Different serialisation formats metric"
metric_multiple_types = "Instances with multiple types metric"

# Likert mapping functions
def map_direct_0_1(num):
    if num > 1: return 5
    if num < 0.2: return 1
    if num < 0.4: return 2
    if num < 0.6: return 3
    if num < 0.8: return 4
    return 5

def map_inverse_0_1(num):
    if num > 1: return 1
    if num < 0.2: return 5
    if num < 0.4: return 4
    if num < 0.6: return 3
    if num < 0.8: return 2
    return 1

def map_multiple_types(num):
    if num == 0: return 3
    if num <= 1: return 4
    return 5

# Set parsing function
def parse_set_count(val):
    s = val.strip()

    if s.lower() == "set()":
        return 0

    if s.lower().startswith("set(") and s.endswith(")"):
        inside = s[s.find("(")+1:-1].strip()
        if inside == "":
            return 0
        return len([x for x in inside.split(",") if x.strip()])

    if s.startswith("{") and s.endswith("}"):
        inside = s[1:-1].strip()
        if inside == "":
            return 0
        return len([x for x in inside.split(",") if x.strip()])

    return 1

def map_serialization_formats(val_str):
    count = parse_set_count(val_str)

    if count == 0: return 1
    if count == 1: return 3
    if count == 2: return 4
    return 5


# Read all CSV files in the input directory and store their rows and headers
all_rows = []
headers = {}

input_files = list(input_dir.glob("*.csv"))

for file in input_files:
    with file.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        headers[file] = header

        for row in reader:
            if row:
                all_rows.append((header, row))


# Calculate min and max values for metrics that need normalization from 0 to infinity
min_vals = {m: float("inf") for m in mapping_zero_to_infinity}
max_vals = {m: float("-inf") for m in mapping_zero_to_infinity}

for header, row in all_rows:
    for i, v in enumerate(row):
        if i == 0:
            continue

        metric = header[i] if i < len(header) else ""

        if metric in mapping_zero_to_infinity:
            try:
                num = float(v)
                min_vals[metric] = min(min_vals[metric], num)
                max_vals[metric] = max(max_vals[metric], num)
            except:
                pass


# Normalisation function for metrics that need to be normalized from 0 to infinity
def normalize_minmax(num, metric):
    min_v = min_vals.get(metric)
    max_v = max_vals.get(metric)

    if min_v is None or max_v is None:
        return num

    if max_v == min_v:
        # return 0.0 # if all values are the same, return None instead of 0.0 to avoid skewing the normalisation
        
        return None


    return (num - min_v) / (max_v - min_v)


# Principal function to map values to Likert scale based on metric type
def map_value(val, metric_name):

    if val is None or str(val).strip() == "":
        return ""

    val_str = str(val).strip()
    val_low = val_str.lower()

    # Boolean mapping
    if val_low == "true": return 5
    if val_low == "false": return 1

    # Serialisation mapping
    if metric_name == metric_serialization:
        return map_serialization_formats(val_str)

    # Multipple types mapping
    if metric_name == metric_multiple_types:
        try:
            num = float(val_str)
        except:
            return val
        return map_multiple_types(num)

    # Sets mapping
    if val_low.startswith("set(") or (val_low.startswith("{") and val_low.endswith("}")):
        return 1 if val_low == "set()" else 5

    # Numeric
    try:
        num = float(val_str)
    except:
        return val

    # Normalise metrics that need to be normalized from 0 to infinity
    if metric_name in mapping_zero_to_infinity:
        #num = normalize_minmax(num, metric_name) # if num is None, return 3, to avoid skewing the normalisation
        num_norm = normalize_minmax(num, metric_name)    
        if num_norm is None:
            return 3
        num = num_norm

    # Map to Likert scale based on metric type
    if metric_name in mapping_inverse:
        return map_inverse_0_1(num)

    return map_direct_0_1(num)


# Process each input file, normalise the metrics and map them to Likert scale, then save the output to a new CSV file
for file in input_files:

    print(f"Processing {file.name}")

    #base_name = file.stem.removeprefix("combined_")
    base_name = file.stem.removesuffix("_results")
    output_file = outdir / f"{base_name}_metrics_likert.csv"
    #output_file = outdir / "metrics_likert.csv"

    with file.open(newline="", encoding="utf-8") as infile, \
         output_file.open("w", newline="", encoding="utf-8") as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            new_row = []

            for i, v in enumerate(row):
                if i == 0:
                    new_row.append(v)
                else:
                    metric_name = header[i] if i < len(header) else ""
                    new_row.append(map_value(v, metric_name))

            writer.writerow(new_row)

    print(f"Save in {output_file}")

print("Process completed")
