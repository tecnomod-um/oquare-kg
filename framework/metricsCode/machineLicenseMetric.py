from rdflib import Graph, URIRef, Literal, DCTERMS

# Define the set of defined license predicates (as URIRefs).
defined_license_predicates = {
    URIRef("http://creativecommons.org/ns#license"),
    DCTERMS.license,
    URIRef("http://www.w3.org/1999/xhtml/vocab#license"),
    # Add other relevant license predicates here
}

# Define the set of valid machine-readable licenses (as URIRefs).
valid_machine_licenses = {
    URIRef("http://creativecommons.org/licenses/by/4.0/"),
    URIRef("http://creativecommons.org/licenses/by-sa/4.0/"),
    URIRef("http://creativecommons.org/licenses/by-nc/4.0/"),
    # Add other valid machine-readable licenses here
}

def licensePred(predicate):
    """Checks if the predicate is a defined license predicate."""
    return predicate in defined_license_predicates

def licenseValid(obj):
    """Checks if the object is a valid machine-readable license."""
    return obj in valid_machine_licenses

def machine_license_metric(graph):
    """
    Checks license compliance of triples in an RDF graph.

    Args:
        graph: RDF graph.

    Returns:
        The metric calculates the ratio of compliant triples to total triples. Best = 1
    """
    compliant_triples = 0
    total_triples = 0

    for subject, predicate, obj in graph:
        total_triples += 1
        if licensePred(predicate) and licenseValid(obj):
            compliant_triples += 1

    if total_triples > 0:
        valid_licenses_metric = compliant_triples / total_triples
    else:
        valid_licenses_metric = 0

    return valid_licenses_metric