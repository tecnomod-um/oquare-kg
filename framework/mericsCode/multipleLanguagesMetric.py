from rdflib import Graph, RDF, RDFS, Literal, URIRef, SKOS

def multiple_languages_metric(graph):
    """
    Calculates the ratio of labels with a language tag.

    Args:
        graph: RDF graph.

    Returns:
        Ratio of language-tagged labels to total labels. Best = 1
    """

    if not graph:
        return 0.0  # If the graph is empty

    language_label_count = 0
    total_label_count = 0
    label_predicates = {RDFS.label, SKOS.prefLabel, SKOS.altLabel} # set of synonym predicates, add as many as necessary

    for subject, predicate, obj in graph:
        if predicate in label_predicates and isinstance(obj, Literal):
            total_label_count += 1
            if obj.language:
                language_label_count += 1

    if total_label_count > 0:
        languages_metric = language_label_count / total_label_count
    else:
        languages_metric = 0

    return languages_metric