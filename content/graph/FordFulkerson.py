"""
 * Author: Unknown
 * Source: https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
 * Description: Computes maximum flow. Uses weight as capacity.
 Null weighted edges must already be integrated into the graph.
 Add "and graph.edges[u][neighbor] > 0" to the condition at line 14 in BFS.py.
 Graph is modified.
 * Time: O(VE)
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
