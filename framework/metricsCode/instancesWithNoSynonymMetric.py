from rdflib import SKOS, RDF

def instances_without_synonyms_metric(graph):
    """

    Calculates the ratio of instances without description used in a graph.

    Args:
        graph: RDFlib graph.

    Returns:
        Mean number of instances without synonym. Best = O
    """
    instances = set()
    instances_with_synonym = set()
    synonym_predicates = {SKOS.altLabel, SKOS.hiddenLabel}  # set of synonym predicates, add as many as necesary

    # Find the instances (rdf:type predicates)
    for subject, predicate, obj in graph:
        if predicate == RDF.type:
            instances.add(subject)
    # Find instances with description
        elif predicate in synonym_predicates:
            instances_with_synonym.add(subject)

    # Calculate the ratio of instances without description
    no_synonyms_count = len(instances - instances_with_synonym)
    total_instances = len(instances)

    if no_synonyms_count > 0:
        without_synonyms = no_synonyms_count / total_instances
    else:
        without_synonyms = 0
   
    return without_synonyms