
# OQuaRE-KG package


from .evaluation import evaluate
from .scores import scoring
import argparse


def run_oquarekg(
    graph_file,
    domain_uri,
    output_dir="results"
):
    """
    Execute complete OQuaRE-KG workflow.
    """

    evaluate(
        graph_file=graph_file,
        domain_uri=domain_uri,
        output_dir=output_dir
    )

    scoring(
        input_dir=output_dir,
        output_dir=output_dir
    )


def main():
    """
    Command-line entry point for the complete workflow.
    """

    parser = argparse.ArgumentParser(
        description="Execute complete OQuaRE-KG workflow"
    )

    parser.add_argument(
        "graph_file",
        help="Path to RDF graph"
    )

    parser.add_argument(
        "--domain-uri",
        required=True,
        help="Domain URI"
    )

    parser.add_argument(
        "--output-dir",
        default="results",
        help="Output directory"
    )

    args = parser.parse_args()

    run_oquarekg(
        graph_file=args.graph_file,
        domain_uri=args.domain_uri,
        output_dir=args.output_dir
    )