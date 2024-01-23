"""
 * Author: Unknown
 * Source: https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/ 
 * Description: Computes shortest paths from $start$. Allows negative-weighted cycles
 * Time: $O(VE)$
"""
def bellmanFord(graph, start_vertex):
    distance = [float("inf") for _ in range(graph.v)]
    distance[start_vertex] = 0
    for _ in range(graph.v - 1):
        for u, v, w in graph.get_weighted_edges():
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    for _ in range(graph.v - 1):
        for u, v, w in graph.get_weighted_edges():
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                distance[v] = -float("inf")
    return distance
