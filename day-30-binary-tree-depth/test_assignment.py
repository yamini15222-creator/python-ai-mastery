"""Tests for binary-tree hierarchy depth."""

import pytest
from assignment import (
    HierarchyCycleError,
    TreeNode,
    hierarchy_depth,
    hierarchy_depth_iterative,
    max_depth_bfs,
)


def test_empty_tree():
    """An empty tree has depth zero."""
    assert hierarchy_depth(None) == 0


def test_single_node():
    """A single node has depth one."""
    root = TreeNode(1)

    assert hierarchy_depth(root) == 1


def test_balanced_three_level_tree():
    """A balanced three-level tree has depth three."""

    root = TreeNode(
        1,
        left=TreeNode(2),
        right=TreeNode(3),
    )

    assert hierarchy_depth(root) == 2


def test_three_level_tree():
    """A tree with three employee levels has depth three."""

    root = TreeNode(
        1,
        left=TreeNode(
            2,
            left=TreeNode(4),
            right=TreeNode(5),
        ),
        right=TreeNode(3),
    )

    assert hierarchy_depth(root) == 3


def test_skewed_tree():
    """A four-node skewed tree has depth four."""

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)

    assert hierarchy_depth(root) == 4


def test_uneven_tree():
    """An uneven tree returns the deepest branch."""

    root = TreeNode(
        1,
        left=TreeNode(2),
        right=TreeNode(
            3,
            left=TreeNode(
                4,
                left=TreeNode(5),
            ),
        ),
    )

    assert hierarchy_depth(root) == 4


def test_left_skewed_tree():
    """A left-only hierarchy is handled correctly."""

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)

    assert hierarchy_depth(root) == 3


def test_original_tree_is_not_modified():
    """Depth calculation must not modify the tree."""

    child = TreeNode(2)
    root = TreeNode(1, left=child)

    hierarchy_depth(root)

    assert root.left is child
    assert root.left.employee_id == 2


def test_recursive_and_iterative_match():
    """Recursive and iterative DFS must return the same result."""

    root = TreeNode(
        1,
        left=TreeNode(
            2,
            left=TreeNode(4),
        ),
        right=TreeNode(
            3,
            right=TreeNode(
                5,
                right=TreeNode(6),
            ),
        ),
    )

    assert hierarchy_depth(root) == hierarchy_depth_iterative(root)


def test_recursive_and_bfs_match():
    """Recursive DFS and BFS must return the same depth."""

    root = TreeNode(
        1,
        left=TreeNode(2),
        right=TreeNode(
            3,
            left=TreeNode(4),
            right=TreeNode(5),
        ),
    )

    assert hierarchy_depth(root) == max_depth_bfs(root)


def test_all_three_implementations_match():
    """DFS recursive, DFS iterative and BFS must agree."""

    root = TreeNode(
        1,
        left=TreeNode(
            2,
            left=TreeNode(4),
            right=TreeNode(5),
        ),
        right=TreeNode(
            3,
            right=TreeNode(6),
        ),
    )

    assert hierarchy_depth(root) == hierarchy_depth_iterative(root)
    assert hierarchy_depth(root) == max_depth_bfs(root)


def test_cycle_is_detected():
    """Recursive DFS detects a cycle."""

    root = TreeNode(1)
    child = TreeNode(2)

    root.left = child
    child.left = root

    with pytest.raises(HierarchyCycleError):
        hierarchy_depth(root)


def test_bfs_cycle_is_detected():
    """BFS detects repeated nodes."""

    root = TreeNode(1)
    child = TreeNode(2)

    root.left = child
    child.left = root

    with pytest.raises(HierarchyCycleError):
        max_depth_bfs(root)


def test_iterative_cycle_is_detected():
    """Iterative traversal detects repeated nodes."""

    root = TreeNode(1)
    child = TreeNode(2)

    root.left = child
    child.left = root

    with pytest.raises(HierarchyCycleError):
        hierarchy_depth_iterative(root)