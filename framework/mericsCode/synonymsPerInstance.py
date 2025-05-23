from rdflib import Graph, RDF, URIRef

def synonyms_per_instance_metric(graph):
    """
    Calculates the synonyms per instance metric for an RDF graph.

    Args:
        graph: RDF graph.
        
    Returns:
        The synonyms per instance metric. Best = 1
    """

    total_synonyms = 0
    total_instances = 0

    # Define a default set of synonym properties
    synonym_properties = {
        URIRef("http://www.w3.org/2004/02/skos/core#altLabel"),
        URIRef("http://www.w3.org/2004/02/skos/core#hiddenLabel"),
        # Add other common synonym properties here
    }

    # Count synonyms
    for subject, predicate, obj in graph:
        if isinstance(subject, URIRef) and predicate in synonym_properties:
            total_synonyms += 1
        elif predicate == RDF.type and isinstance(subject, URIRef):    # Count instances
            total_instances += 1

    # Calculate metric
    if total_instances > 0:
        synonyms_metric = total_synonyms / total_instances
    else:
        synonyms_metric = 0

    return synonyms_metric