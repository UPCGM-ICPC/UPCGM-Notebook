"""
 * Author: Yanis Lacenne
 * Source: https://en.wikipedia.org/wiki/Breadth-first_search
 * Description: Finds a path between using BFS. Returns list of parent's indexes
 per node if a path between source $s$ and sink $t$ exists, None otherwise.
 * Time: O(V+E)
"""
def BFS(graph, s, t):
    visited = [False for _ in range(len(graph.v))]
    visited[s] = True
    queue, parent = [s], [-1] * len(graph.v)
    while queue:
        u = queue.pop(0)
        for neighbor in graph.get_neighbors(u):
            if (not visited[neighbor]):
                queue.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = u
                if neighbor == t:
                    return parent
    return None
