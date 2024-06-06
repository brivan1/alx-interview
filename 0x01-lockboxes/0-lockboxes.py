#!/usr/bin/python3
"""
lockbox module
"""


def canUnlockAll(boxes):
    """
    function to check whether all the boxes have been opened or can they be
    opened with the provided key
    """

    n = len(boxes)
    visited = set([0])
    not_visited = set(boxes[0]).difference(set([0]))
    while len(not_visited) > 0:
        box = not_visited.pop()
        if not box or box >= n or box < 0:
            continue
        if box not in visited:
            not_visited = not_visited.union(boxes[box])
            visited.add(box)
    return n == len(visited)
