import csv
from pathlib import Path
from rdflib import Graph
from rdflib.util import guess_format
from typing import Tuple, Dict, List
import argparse
from .metrics import *


def evaluate_graph(graph_path: Path, domain_uri: str) -> Tuple[Graph, str, int]:
    graph = Graph()
    fmt = guess_format(str(graph_path))

    if not fmt:
        raise ValueError(f"Could not determine the format of the file: {graph_path}")
    
    graph.parse(str(graph_path), format=fmt)

    triple_count = len(graph)
    print(f"Graph loaded from {graph_path} ({fmt}) with {triple_count} triples")
    return graph, fmt, triple_count


def run_metrics(graph: Graph, metric_list, graph_path: Path, output_dir: Path) -> Dict[str, float]:
    """
    Runs metrics and saves the results in wide format: oquareKG_results.csv
    Returns results dictionary (for combined CSV)
    """

    results = {}

    for metric in metric_list:
        metric_name = metric.get_metric_name()
        metric_value = metric.calculate_metric(graph)
        print(f"{metric_name} = {metric_value}")
        results[metric_name] = metric_value

    output_dir.mkdir(exist_ok=True)
    graph_name = graph_path.stem

    return results


def save_results_wide(all_results: Dict[str, Dict[str, float]], output_dir: Path):
    """
    Creates one CSV in wide format, in case of multiple graphs, the CSV will have multiple rows
    """

    if not all_results:
        return
    
    output_csv = output_dir / f"oquareKG_results.csv" 

    # Get all unique metric names across all graphs
    all_metrics = set()
    for res in all_results.values():
        all_metrics.update(res.keys())

    all_metrics = sorted(all_metrics)

    with output_csv.open("w", newline="") as f:
        writer = csv.writer(f)

        # header
        writer.writerow(["graph"] + all_metrics)

        # rows
        for graph_name, res in all_results.items():
            row = [graph_name]
            for m in all_metrics:
                row.append(res.get(m, ""))  # por si falta alguna métrica
            writer.writerow(row)

    print(f"OQuaRE-KG results CSV saved in {output_csv}")


def evaluate(
    graph_file,
    domain_uri,
    output_dir="results"
):
    """
    Evaluate one RDF graph.
    """

    results_folder = Path(output_dir)

    results_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    graph_path = Path(graph_file)

    graph, graph_format, triple_count = evaluate_graph(
        graph_path,
        domain_uri
    )


    metric_list = [
                AnnotationRichnessMetric(),
                BasicProvenanceMetric(),
                ClassesPerInstanceMetric(),
                CompatibleDatatypeMetric(),
                DeprecatedTermsMetric(),
                DereferenceabilityMetric(),
                DescriptionsPerInstanceMetric(),
                DifferentSerializationFormatsMetric(),
                EntitiesNoTypeMetric(),
                EvidenceMetric(),
                ExtensionalConcisenessMetric(),
                HumanReadableLicenseMetric(),
                InstancesMultipleTypesMetric(),
                InstancesWithNoDescriptionMetric(),
                InstancesWithNoNameMetric(),
                InstancesWithNoSynonymMetric(),
                MachineLicenseMetric(),
                MisplacedClassPropertyMetric(),
                MisusedPropertiesMetric(),
                MultipleLanguagesMetric(),
                NamesPerInstanceMetric(),
                RelationsPerNodeMetric(),
                ReuseTermsMetric(domain=domain_uri),
                SynonymsPerInstanceMetric(),
                TraceabilityDataMetric(),
                UsageUndefinedTermsMetric(),
                UsedVocabulariesMetric(),
                ValidFormatMetric(input_format=graph_format),
    ]

    results = run_metrics(
        graph,
        metric_list,
        graph_path,
        results_folder
    )

    save_results_wide(
        {graph_path.stem: results},
        results_folder
    )

    return results




def main():
    """
    Command line entry point.
    """

    parser = argparse.ArgumentParser(
        description="Evaluate RDF graphs"
    )

    parser.add_argument(
        "graph_file"
    )

    parser.add_argument(
        "--domain-uri",
        required=True
    )

    parser.add_argument(
        "--output-dir",
        default="results"
    )

    args = parser.parse_args()

    evaluate(
        graph_file=args.graph_file,
        domain_uri=args.domain_uri,
        output_dir=args.output_dir
    )

    if __name__ == "__main__":
        main()