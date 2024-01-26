"""
 * Author: Unknown
 * Source: https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
 * Description: Computes maximum flow. Uses weight as capacity.
 Condition on positive weight should be added in GraphClass.
"""
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
