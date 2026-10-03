"""Binary-tree hierarchy depth algorithms."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass
class TreeNode:
    """Represent an employee in a binary hierarchy."""

    employee_id: int
    left: TreeNode | None = None
    right: TreeNode | None = None


class HierarchyCycleError(ValueError):
    """Raised when a cycle is detected in the hierarchy."""


def hierarchy_depth(root: TreeNode | None) -> int:
    """Return the maximum depth of a binary hierarchy using recursive DFS.

    Depth is measured by the number of nodes on the longest path
    from the root to a leaf.

    An empty tree has depth 0.
    A single-node tree has depth 1.

    Args:
        root: Root employee of the hierarchy.

    Returns:
        Maximum number of nodes from root to a leaf.

    Raises:
        HierarchyCycleError: If a cycle is detected.
    """

    active_path: set[int] = set()

    def dfs(node: TreeNode | None) -> int:
        if node is None:
            return 0

        node_identity = id(node)

        if node_identity in active_path:
            raise HierarchyCycleError(
                "Cycle detected in organization hierarchy"
            )

        active_path.add(node_identity)

        left_depth = dfs(node.left)
        right_depth = dfs(node.right)

        active_path.remove(node_identity)

        return 1 + max(left_depth, right_depth)

    return dfs(root)


def hierarchy_depth_iterative(
    root: TreeNode | None,
) -> int:
    """Return maximum hierarchy depth using iterative DFS.

    This avoids Python recursion-depth limitations on very deep
    hierarchies.
    """

    if root is None:
        return 0

    stack = [(root, 1)]
    active_path: set[int] = set()
    maximum_depth = 0

    while stack:
        node, depth = stack.pop()

        if node is None:
            continue

        node_identity = id(node)

        if node_identity in active_path:
            raise HierarchyCycleError(
                "Cycle detected in organization hierarchy"
            )

        maximum_depth = max(maximum_depth, depth)

        if node.right is not None:
            stack.append((node.right, depth + 1))

        if node.left is not None:
            stack.append((node.left, depth + 1))

    return maximum_depth


def max_depth_bfs(
    root: TreeNode | None,
) -> int:
    """Return maximum hierarchy depth using breadth-first search."""

    if root is None:
        return 0

    queue = deque([root])
    depth = 0
    visited: set[int] = set()

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            node_identity = id(node)

            if node_identity in visited:
                raise HierarchyCycleError(
                    "Cycle or repeated node detected"
                )

            visited.add(node_identity)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        depth += 1

    return depth