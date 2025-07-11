from rdflib import Graph, URIRef, DCTERMS, Literal

def basic_provenance_metric(graph):
    """
    Calculates the percentage of provenance and authoring predicates used in a RDF graph.

    Args:
        graph: RDF graph.

    Returns:
        The ratio of predicates used in the graph. Best = 1
    """

    basic_prov_predicates = {
        DCTERMS.creator,
        DCTERMS.publisher,
        URIRef("http://purl.org/pav/providedBy")
    }
    # basic provenance predicates used in the graph
    used_prov_predicates = set()

    for subject, predicate, obj in graph:
        if predicate in basic_prov_predicates:
            used_prov_predicates.add(predicate)

    if len(used_prov_predicates) > 0:
        basic_prov_metric = (len(used_prov_predicates) / len(basic_prov_predicates))
    else:
        basic_prov_metric = 0.0

    return basic_prov_metric
