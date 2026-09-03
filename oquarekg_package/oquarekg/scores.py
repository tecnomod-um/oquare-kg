import argparse
from pathlib import Path
import subprocess

# the input file must be in wide format, with the metrics in columns and the graphs in rows.


# Directory of this file (scaling.py)
BASE_DIR = Path(__file__).parent

# Directory containing the scaling scripts
SCRIPTS_DIR = BASE_DIR / "calculate_scores"

def run_script(script, input_file, output_file):
    """
    Executes a script with the given input and output files.
    """
    print(f"   → {script.name}")

    subprocess.run(
        [
            "python",
            str(script),
            "--input", str(input_file),
            "--output", str(output_file)
        ],
        check=True
    )


def process_one_file(input_file, outdir):
    """
    Execute the pipeline for a single input file at a time.
    """

    print(f"\n Processing files: {input_file.name} ") 


# Remove suffixes from the input file name to create a base name for output files
    name = (
        input_file.stem
        #.removeprefix("oquareKG_")
        .removesuffix("_metrics_likert")
        .removesuffix("_subcharacteristics_likert")
    )

# Sufixes for outputs
    out1 = outdir / f"{name}_subcharacteristics_likert.csv"
    out2 = outdir / f"{name}_characteristics_likert.csv"

    # input_file is metrics_likert.csv, output_file is subcharacteristics_likert.csv
    run_script(SCRIPTS_DIR / "calculateSubcharacteristics.py", input_file, out1) 

    # input_file is subcharacteristics_likert.csv, output_file is characteristics_likert.csv
    run_script(SCRIPTS_DIR / "calculateCharacteristics.py", out1, out2) 

    print("\nPipeline completed successfully.")



def scoring(
    input_dir,
    output_dir
):
    """
    Execute complete scoring workflow.
    """
    # Convert strings to Path objects
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

# Convert strings to Path objects




    # Calculate Likert scores for metrics

    print("Calculating Likert scores for metrics...")

    subprocess.run(
        [
            "python",
            str(SCRIPTS_DIR / "calculateMetricsLikert.py"),
            "--input_dir",
            str(input_dir),
            "--outdir",
            str(output_dir)
        ],
        check=True
    )

    # Process generated metric files

    input_files = list(
        output_dir.glob("*_metrics_likert.csv")
    )

    print("Starting processing of files...")
    print(f"Found {len(input_files)} files to process")

    for input_file in input_files:
        process_one_file(
            input_file,
            output_dir
        )

    print("\nAll datasets processed.")

def main():

    parser = argparse.ArgumentParser(
        description="Pipeline calculate Likert scores"
    )

    parser.add_argument(
        "--input_dir",
        type=Path,
        required=True,
        help="CSV files directory"
    )

    parser.add_argument(
        "--outdir",
        type=Path,
        required=True,
        help="Output directory"
    )

    args = parser.parse_args()

    scoring(
        input_dir=args.input_dir,
        output_dir=args.outdir
    )


if __name__ == "__main__":
    main()

