from abc import ABC
from typing import Union, Set
from rdflib import Graph

class Metric(ABC):
    def calculate_metric(self, graph: Graph) -> Union[float, bool, Set]: # all possible values
        pass

    def get_metric_name(self) -> str:
        pass

