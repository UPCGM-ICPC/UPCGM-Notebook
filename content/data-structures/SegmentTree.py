"""
* Author: AnkitRai01
* Description: Segment tree implementation. ranged are [l, r[
* Source: https://www.geeksforgeeks.org/segment-tree-efficient-implementation/
* Time: O(log(n))
"""
N = 100000 # Max size of tree
tree = [0] * (2 * N)
def build(arr): # function to build the tree
    # insert leaf nodes in tree, n is global
    for i in range(n):
        tree[n + i] = arr[i]
    # build the tree by calculating parents
    for i in range(n - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]
def updateTreeNode(p, value): # function to update a tree node
    tree[p + n] = value ; p = p + n; i = p
    while i > 1:
        tree[i >> 1] = tree[i] + tree[i ^ 1]
        i >>= 1
def query(l, r): # function to get sum on interval [l, r)
    res = 0; l += n; r += n
    while l < r:
        if l & 1:
            res += tree[l]
            l += 1
        if r & 1:
            r -= 1
            res += tree[r]
        l >>= 1; r >>= 1
    return res
