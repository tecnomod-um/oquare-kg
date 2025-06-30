from rdflib import Graph, URIRef, Literal, RDF

def descriptions_per_instance_metric(graph):
    """
    Calculates the descriptions per instance metric for a RDF graph.

    Args:
        graph: RDF graph.
        
    Returns:
        The descriptions per instance metric. Best >= 1
    """

    total_descriptions = 0
    total_instances = set()  

    # Define a default set of description predicates. As many as needed
    description_predicates = {
        URIRef("http://schema.org/description"),
        URIRef("http://purl.org/dc/terms/description"),
        URIRef("http://www.w3.org/2000/01/rdf-schema#comment"),
    }

    for subject, predicate, obj in graph:
        # Check if the predicate is a description predicate
        if predicate in description_predicates and isinstance(subject, URIRef):
            total_descriptions += 1

        # Count instances only if they have an rdf:type
        if predicate == RDF.type and isinstance(subject, URIRef):
            total_instances.add(subject)

    #num_total_descriptions = len(total_descriptions)
    num_total_instances = len(total_instances)

    if num_total_instances > 0:
        descriptions_metric = total_descriptions / num_total_instances
    else:
        descriptions_metric = 0

    return descriptions_metric