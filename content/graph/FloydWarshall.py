""" 
* Author: Yago Iglesias
 * Date: 2016-12-15
 * License: CC0
 * Source: http://en.wikipedia.org/wiki/Floyd–Warshall_algorithm
 * Description: Calculates all-pairs shortest path in a directed graph that might have negative edge weights.
 * As output, $m[i][j]$ is set to the shortest distance between $i$ and $j$ and \texttt{INF} if no path.
 * Time: O(N^3)
 * Status: slightly tested
"""
INF = 1 << 62  # Large enough value for unreachable vertices
def floydWarshall(self):
    dist = [[INF] * self.v for _ in range(self.v)]
    for u in range(self.v):  # Diagonal
        dist[u][u] = 0
    for u in range(self.v):  # Edges
        for v in self.edges[u]:
            dist[u][v] = self.edges[u][v]
    for k in range(self.v):
        for i in range(self.v):
            for j in range(self.v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
