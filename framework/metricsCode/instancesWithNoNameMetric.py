from rdflib import RDF, RDFS, DCTERMS, FOAF

def instances_without_name_metric(graph):
    """

    Calculates the ratio of instances without a name used in a graph.

    Args:
        graph: RDF graph.

    Returns:
        Mean number of instances without a name. Best = 0
    """
  
    instances = set()
    named_instances = set()
    name_predicates = {RDFS.label, DCTERMS.title, FOAF.name}  # set of names predicates, add as many as necesary

    # Find the instances (rdf:type predicates)
    for subject, predicate, obj in graph:
        if predicate == RDF.type:
            instances.add(subject)
    # Find instances with name
        elif predicate in name_predicates:
            named_instances.add(subject)

    # Calculate the ratio of instances without name
    unnamed_count = len(instances - named_instances)
    total_instances = len(instances)

    if unnamed_count > 0:
        without_name = (unnamed_count / total_instances)
    else:
        without_name = 0

    return without_name