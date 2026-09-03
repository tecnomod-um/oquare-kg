from rdflib import DC, DCTERMS, Graph, URIRef, Literal
from .metric import Metric
from ..predicates import LICENSE_PREDICATES, MACHINE_LICENSES

class MachineLicenseMetric(Metric):
    # Define the set of defined license predicates (as URIRefs).
    # defined_license_predicates = {
    #     URIRef("http://creativecommons.org/ns#license"),
    #     DCTERMS.license,
    #     DC.rights,
    #     DCTERMS.rights,
    #     URIRef("https://schema.org/license"),
    #     URIRef("http://www.w3.org/1999/xhtml/vocab#license"),
    #     # Add other relevant license predicates here
    # }

    # Define the set of valid machine-readable licenses (as URIRefs).
    # valid_machine_licenses = {
    #     URIRef("http://creativecommons.org/licenses/by/4.0/"),
    #     URIRef("http://creativecommons.org/licenses/by-sa/4.0/"),
    #     URIRef("http://creativecommons.org/licenses/by-nc/4.0/"),
    #     # Add other valid machine-readable licenses here
    # }

    def licensePred(predicate):
        """Checks if the predicate is a defined license predicate."""
        return predicate in LICENSE_PREDICATES

    def licenseValid(obj):
        """Checks if the object is a valid machine-readable license."""
        return obj in MACHINE_LICENSES

    def calculate_metric(self, graph: Graph) -> bool:
        """
        Checks license compliance of triples in an RDF graph.

        Args:
            graph: RDF graph.

        Returns:
            True if a valid machine-readable license is found, False otherwise. Best = true
        """


        for subject, predicate, obj in graph:
            if MachineLicenseMetric.licensePred(predicate) and MachineLicenseMetric.licenseValid(obj):
                return True
        return False

    
    def get_metric_name(self):
        return 'Machine license metric'