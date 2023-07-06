#!/usr/bin/python3
"""Lockboxes challenge solution"""


def canUnlockAll(boxes):
    """Main logic"""
    n = len(boxes)
    visited = [False] * n

    def dfs(box):
        """depth-first search algorithm"""
        visited[box] = True
        for key in boxes[box]:
            if not visited[key]:
                dfs(key)

    dfs(0)

    # check if all boxes were visited
    return all(visited)
