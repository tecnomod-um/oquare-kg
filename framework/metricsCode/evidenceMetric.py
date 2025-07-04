from rdflib import Graph, RDF, RDFS, DCTERMS, URIRef, OWL, Literal
from rdflib.namespace import Namespace

# Define the ECO namespace
ECO = Namespace("http://purl.obolibrary.org/obo/ECO_")

# Mapping of GO Evidence Codes to ECO IDs 
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

def evidence_metric(graph):
    """
    Calculates the ratio of triples with predicates whose objects are
    specific GO or ECO evidence URIs, in relation to the total number of triples
    defining instances in the graph.

    Args:
        graph: A RDFlib Graph.

    Returns:
        The ratio of triples with valid GO/ECO evidence. Best = 1.
    """
    total_instances = 0
    triples_with_valid_evidence = 0

    # Set of common evidence related predicates.
    # Add any other specific predicates that indicate evidence.
    evidence_predicates = {
        URIRef("http://geneontology.org/lego/evidence"),
        URIRef("http://geneontology.org/lego/evidence-with"),
        DCTERMS.source,
        DCTERMS.references,
        RDFS.isDefinedBy,
        OWL.sameAs,
        URIRef("http://purl.org/dc/elements/1.1/source"),
    }

    for subject, predicate, obj in graph:
        # Count declarations of instances
        if predicate == RDF.type and isinstance(subject, URIRef):
            total_instances += 1

        # Check if the predicate is an evidence predicate and the object is a valid ECO URI
        if predicate in evidence_predicates and isinstance(obj, URIRef) and str(obj) in valid_eco_uris:
            triples_with_valid_evidence += 1

    if total_instances > 0:
        evidence_metric = triples_with_valid_evidence / total_instances
    else:
        evidence_metric = 0

    return evidence_metric
