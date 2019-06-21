from unittest import TestCase
from problem_solving.graph.route_between_nodes import route_between_nodes


class TestGraph(TestCase):

    def test_route_between_nodes(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['C', 'F'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C'],
            'K': ['F']
        }
        self.assertEqual(route_between_nodes(graph, 'A', 'K'), False)
        self.assertEqual(route_between_nodes(graph, 'A', 'D'), True)
