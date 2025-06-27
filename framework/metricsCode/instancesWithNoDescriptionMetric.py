from rdflib import Graph, RDF, RDFS, DCTERMS, URIRef

def instances_without_description_metric(graph):
    """
    Calculates the ratio of instances without description used in a graph.

    Args:
        graph: RDFlib graph.

    Returns:
        Ratio of instances without description. Best = 0
    """
    instances = set()
    described_instances = set()
    description_predicates = {RDFS.comment, DCTERMS.description}

    for subject, predicate, obj in graph:
        if isinstance(subject, URIRef):
            if predicate == RDF.type:
                instances.add(subject)
            elif predicate in description_predicates:
                described_instances.add(subject)

    undescribed_count = len(instances - described_instances)
    total_instances = len(instances)

    if total_instances > 0:
        without_description = undescribed_count / total_instances
    else:
        without_description = 0

    return without_description