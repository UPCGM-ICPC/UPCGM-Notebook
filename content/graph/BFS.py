"""
 * Author: Yanis Lacenne
 * Source: https://en.wikipedia.org/wiki/Breadth-first_search
 * Description: Finds path between using BFS. Returns list of parent's index
 per node if path between source $s$ and sink $t$ exists, None otherwise.
"""
from GraphClass import Graph
def BFS(graph, s, t):
    visited = [False for _ in range(len(graph.v))]
    visited[s] = True
    queue, parent = [s], [-1] * len(graph.v)
    while queue:
        u = queue.pop(0)
        for neighbor in graph.get_neighbors(u):
            if (not visited[neighbor]) and graph.edges[u][neighbor] > 0:
                queue.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = u
                if neighbor == t:
                    return parent
    return None


if __name__ == "__main__":
    graph = Graph([0, 1, 2, 3, 4, 5], [(0, 1, 16), (1, 0, 0), (0, 2, 13),
                                       (2, 0, 0), (1, 2, 10), (2, 1, 4),
                                       (1, 3, 12), (3, 1, 0), (3, 2, 9),
                                       (2, 3, 0), (2, 4, 14), (4, 2, 0),
                                       (4, 3, 7), (3, 4, 0), (3, 5, 20),
                                       (5, 3, 0), (4, 5, 4), (5, 4, 0)])
    print(BFS(graph, 0, 5))
