"""This module contains the solution for one of the Level 4 problems."""

from collections import deque

def bfs(rGraph, s, t, parent):
    """
    Returns true if there is a path from source 's' to sink 't' in residual
    graph. Also fills parent[] to store the path
    """
    visited = [False] * len(rGraph)
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.popleft()
        for ind, val in enumerate(rGraph[u]):
            if visited[ind] is False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False

def find_max_flow(rGraph, s, t):
    """Returns the maximum flow from s to t in the given graph"""
    parent = [-1] * len(rGraph)
    max_flow = 0

    while bfs(rGraph, s, t, parent):
        path_flow = float("Inf")
        s = t
        while s != 0:
            path_flow = min(path_flow, rGraph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = t
        while v != 0:
            u = parent[v]
            rGraph[u][v] -= path_flow
            rGraph[v][u] += path_flow
            v = parent[v]

    return max_flow

def solution(entrances, exits, path):
    """
    Returns the maximum number of bunnies that can get through at
    each time step
    """
    # adding a supersource and supersink
    path.insert(0, [0] * len(path[0]))
    path.append([0] * len(path[0]))
    for node in path:
        node.insert(0, 0)
        node.append(0)

    # connecting the supersource to the entrances
    for i in entrances:
        path[0][i + 1] = float("Inf")

    # connecting the exits to the supersink
    for i in exits:
        path[i + 1][-1] = float("Inf")

    return find_max_flow(path, 0, len(path) - 1)
