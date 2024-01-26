"""
 * Author: Unknown
 * Source: https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
 * Description: Computes maximum flow. Uses weight as capacity.
 Condition on positive weight should be added in GraphClass.
"""

from GraphClass import Graph
from BFS import BFS
def FordFulkerson(graph, s, t):
    max_flow = 0
    parents = BFS(graph, s, t)
    while parents:
        path_flow = float("Inf")
        r = t
        while (r != s):
            path_flow = min(path_flow, graph.edges[parents[r]][r])
            r = parents[r]
        max_flow += path_flow
        v = t
        while (v != s):
            u = parents[v]
            graph.edges[u][v] -= path_flow
            graph.edges[v][u] += path_flow
            v = parents[v]
        parents = BFS(graph, s, t)
    return max_flow


if __name__ == "__main__":
    graph = Graph([0, 1, 2, 3, 4, 5], [(0, 1, 16), (1, 0, 0), (0, 2, 13),
                                       (2, 0, 0), (1, 2, 10), (2, 1, 4),
                                       (1, 3, 12), (3, 1, 0), (3, 2, 9),
                                       (2, 3, 0), (2, 4, 14), (4, 2, 0),
                                       (4, 3, 7), (3, 4, 0), (3, 5, 20),
                                       (5, 3, 0), (4, 5, 4), (5, 4, 0)])
    print(FordFulkerson(graph, 0, 5))
