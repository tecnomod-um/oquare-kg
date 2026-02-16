from rdflib import Graph, Literal, URIRef, XSD
from urllib.parse import urlparse

def isCompatible(literal):
    """
    Checks if a literal's datatype is compatible with its lexical form.

    Args:
        literal (rdflib.Literal): The literal.

    Returns:
        bool: True if compatible, False otherwise.
    """


    if not isinstance(literal, Literal):
        return False

    # If there is not a datatype, assume it is a literal string
    if literal.datatype is None:
        return True

    datatype = literal.datatype
    lexical_value = str(literal)

    try:
        if datatype == XSD.integer:
            int(lexical_value)
            return True
        elif datatype == XSD.decimal:
            float(lexical_value)
            return True
        elif datatype == XSD.double:
            float(lexical_value)
            return True
        elif datatype == XSD.boolean:
            if lexical_value.lower() in ["true", "false", "1", "0"]:
                return True
            else:
                return False
        elif datatype == XSD.date:
            from datetime import datetime
            try:
                datetime.strptime(lexical_value, '%Y-%m-%d')
                return True
            except ValueError:
                return False
        elif datatype == XSD.dateTime:
            from datetime import datetime
            try:
                datetime.strptime(lexical_value, '%Y-%m-%dT%H:%M:%S%z')
                return True
            except ValueError:
                try:
                    datetime.strptime(lexical_value, '%Y-%m-%dT%H:%M:%S')
                    return True
                except ValueError:
                    return False

        elif datatype == XSD.anyURI:
            u = urlparse(lexical_value)
            return bool(u.scheme)

        elif datatype == XSD.string:
            return True #strings are always compatible.
        else:
            return False #If the datatype is not one that we specifically check, assume it is not compatible.


    except ValueError:
        return False
    except TypeError:
        return False

def compatible_datatype_metric(graph):
    """
    Calculates the compatibility ratio of literal datatypes in a RDF graph.

    Args:
        graph: RDF graph.

    Returns:
        The compatibility ratio. Best = 1
    """

    valid_literals = 0
    total_literals = 0


    for subject, predicate, obj in graph:
        if isinstance(obj, Literal):
            total_literals += 1
            if isCompatible(obj):
                valid_literals += 1

    if total_literals > 0:
        compatible_datatype = (valid_literals / total_literals)
    else:
        compatible_datatype = 0.0

    return compatible_datatype