from rdflib import Graph, RDF, RDFS, DCTERMS, URIRef, OWL, Literal
from rdflib.namespace import Namespace

""""
# Define the ECO namespace
ECO = Namespace("http://purl.obolibrary.org/obo/ECO_")

# Mapping of GO Evidence Codes to ECO IDs 
# This allows interpreting GO evidence codes as specific ECO types.
# Add as many as necessary
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
"""
evidence_uris = {
    URIRef("http://purl.obolibrary.org/obo/ECO_0000305"),
    URIRef("http://purl.obolibrary.org/obo/ECO_0000314"),
    URIRef("http://purl.obolibrary.org/obo/ECO_0000250"),
    URIRef("http://purl.obolibrary.org/obo/ECO_0000501"),
    URIRef("http://purl.obolibrary.org/obo/ECO_0000304"),
    URIRef("http://purl.obolibrary.org/obo/ECO_0000303"),
}

def calculate_metric(self, graph: Graph) -> float:
    """
    Calculates the average number of evidence URIs associated with instances
    in the graph.

    Args:
        graph: RDF Graph.

    Returns:
        The average number of evidence URIs per instance. Best =< 1
    """
    total_instances = 0
    total_evidence_code_occurrences = 0 # Count each occurrence of a valid ECO code

    # Identify all instances
    instances = set()
    for subject, predicate, obj in graph:
        if predicate == RDF.type and isinstance(subject, URIRef):
            instances.add(subject)
            total_instances += 1

    # Count all occurrences of ECO codes associated with instances
    for subject, predicate, obj in graph:
        # Check if the subject is an identified instance and the object is a evidence URI
        # if subject in instances and isinstance(obj, URIRef) and str(obj) in EvidenceCodesMetric.valid_eco_uris:
        if subject in instances and isinstance(obj, URIRef) and obj in evidence_uris:
            total_evidence_code_occurrences += 1 # Count every time a valid ECO is found

    if total_instances > 0:
        evidence_metric = total_evidence_code_occurrences / total_instances
    else:
        evidence_metric = 0

    return evidence_metric