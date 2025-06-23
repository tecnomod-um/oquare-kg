from rdflib import Graph, RDF, RDFS, DCTERMS, URIRef, OWL, Literal
from rdflib.namespace import Namespace

# Define the ECO namespace
ECO = Namespace("http://purl.obolibrary.org/obo/ECO_")

# === Mapping of GO Evidence Codes to ECO IDs ===
# This allows interpreting GO evidence codes as specific ECO types.
go_to_eco = {
    "IDA": str(ECO["0000314"]), # Inferred from Direct Assay
    "EXP": str(ECO["0000269"]), # Experimental Evidence
    "ISS": str(ECO["0000250"]), # Inferred from Sequence or Structural Similarity
    "IEA": str(ECO["0000501"]), # Inferred from Electronic Annotation
    "TAS": str(ECO["0000304"]), # Traceable Author Statement
    "NAS": str(ECO["0000303"]), # Non-traceable Author Statement
}

# Create a set of valid ECO URIs for quick lookup
valid_eco_uris = set(go_to_eco.values())

def evidence_codes_metric(graph):
    """
    Calculates the average number of valid ECO codes associated with instances
    in the graph.

    Args:
        graph: A RDFlib Graph.

    Returns:
        The average number of valid ECO codes per instance. Best=1
    """
    total_instances = 0
    total_eco_code_occurrences = 0 # Count each occurrence of a valid ECO code

    # Identify all instances
    instances = set()
    for subject, predicate, obj in graph:
        if predicate == RDF.type and isinstance(subject, URIRef):
            instances.add(subject)
            total_instances += 1

    # Count all occurrences of ECO codes associated with instances
    for subject, predicate, obj in graph:
        # Check if the subject is an identified instance and the object is a valid ECO URI
        if subject in instances and isinstance(obj, URIRef) and str(obj) in valid_eco_uris:
            total_eco_code_occurrences += 1 # Count every time a valid ECO is found

    if total_instance_declarations > 0:
        eco_codes_metric = total_eco_code_occurrences / total_instances
    else:
        eco_codes_metric = 0

    return eco_codes_metric
