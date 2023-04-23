"""This module contains the solution for one of the Level 3 problems."""

from collections import deque

def solution(map):
    """
    This function finds the shortest path from the top-left corner to the bottom-right corner
    of a given 2D grid (map) containing 0s (passable) and 1s (walls), with the option to remove
    one wall. Moves can only be made in cardinal directions (up, down, left, or right).
    The function uses a unidirectional Breadth-First Search approach to find the shortest path.

    :param map: A list of lists representing a 2D grid with 0s (passable) and 1s (walls)
    :type map: List[List[int]]
    :return: The length of the shortest path
    :rtype: int
    """
    height = len(map)
    width = len(map[0])

    def neighbors(x, y, removed):
        """
        A generator function that returns the neighbors of a given node (x, y) considering
        if a wall has been removed (removed) or not.

        :param x: The x-coordinate of the current node
        :type x: int
        :param y: The y-coordinate of the current node
        :type y: int
        :param removed: A boolean flag indicating if a wall has been removed
        :type removed: bool
        """
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if nx == width - 1 and ny == height - 1:
                    yield None, None, None, True
                wall = map[ny][nx]
                if not wall or (removed and not wall):
                    yield nx, ny, removed, False
                elif not removed:
                    yield nx, ny, True, False

    visited = set([(0, 0, False)])
    queue = deque([(0, 0, False, 1)])

    while queue:
        x, y, removed, steps = queue.popleft()
        for nx, ny, nremoved, reached in neighbors(x, y, removed):
            if reached:
                return steps + 1
            if (nx, ny, nremoved) not in visited:
                visited.add((nx, ny, nremoved))
                queue.append((nx, ny, nremoved, steps + 1))

    return float('inf')
