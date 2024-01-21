"""
 * Author: Unknown
 * Source: https://www.geeksforgeeks.org/python-program-for-topological-sorting/
 * Description: Topological sorting. Given is an oriented graph. Undefined behavior if the graph is not a DAG.
 It should be put inside the Graph class.
 * Time: $O(|V|+|E|)$
"""
def nonRecursiveTopologicalSortUtil(self, v, visited, stack):
    working_stack = [(v, self.get_neighbors(v))]
    while working_stack:
        v, gen = working_stack.pop()
        visited[v] = True
        for next_neighbor in gen:
            if not visited[next_neighbor]:  # not seen before?
                working_stack.append((v, gen))
                working_stack.append((next_neighbor, self.get_neighbors(next_neighbor)))
                break
        else:
            stack.append(v)
def topologicalSort(self):
    visited = [False] * self.v
    stack = []
    for i in range(self.v):
        if not (visited[i]):
            self.nonRecursiveTopologicalSortUtil(i, visited, stack)
    stack.reverse()
    return stack
