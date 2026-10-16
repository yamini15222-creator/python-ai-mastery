# Day 40 DSA: Balanced Binary Tree — Check Every Node Using Height

## 1. Problem Statement

Determine whether a binary tree is height-balanced.

A binary tree is height-balanced when, at every node:

`abs(left_height - right_height) <= 1`

Both left and right subtrees must also be balanced.

## 2. Height Convention

- Empty subtree: height `0`
- Leaf node: height `1`

Height is measured in nodes, not edges.

## 3. Examples

### Balanced Tree

```text
        1
       / \
      2   3
     /
    4
```

Expected output:

```python
True
```

### Unbalanced Tree

```text
      1
     /
    2
   /
  3
```

Expected output:

```python
False
```

At node `1`, the left height is `2` and the right height is `0`.

Difference = `abs(2 - 0) = 2`

Because the difference exceeds `1`, the tree is unbalanced.

## 4. Algorithm

We use postorder Depth-First Search (DFS).

1. Calculate the left subtree height.
2. If the left subtree is unbalanced, return `-1`.
3. Calculate the right subtree height.
4. If the right subtree is unbalanced, return `-1`.
5. If the height difference exceeds `1`, return `-1`.
6. Otherwise, return `1 + max(left_height, right_height)`.

The helper returns a valid height or `-1` as a failure marker.

The main function returns `True` if the helper result is not `-1`.

## 5. Python Implementation

The complete implementation is available in:

`day_40_balanced_binary_tree.py`

Main function:

```python
def is_balanced(root):
    def checked_height(node):
        if node is None:
            return 0

        left_height = checked_height(node.left)

        if left_height == -1:
            return -1

        right_height = checked_height(node.right)

        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return checked_height(root) != -1
```

## 6. Assignment

### Tree A

```text
          10
         /  \
        4    20
       / \     \
      2   6     30
         /
        5
```

Expected result:

```python
is_balanced(tree_a)  # True
```

### Tree B

Add node `7` as the left child of node `5`.

```text
          10
         /  \
        4    20
       / \     \
      2   6     30
         /
        5
       /
      7
```

Expected result:

```python
is_balanced(tree_b)  # False
```

Node `6` is the first node to detect imbalance during the left-first traversal.

Its left height is `2`, and its right height is `0`.

Difference = `abs(2 - 0) = 2`

Therefore, the helper returns `-1`.

## 7. Test Cases

| Test case | Expected result |
|---|---|
| Empty tree | `True` |
| Single-node tree | `True` |
| Two-node tree | `True` |
| Balanced tree | `True` |
| Unbalanced chain | `False` |
| Assignment Tree A | `True` |
| Assignment Tree B | `False` |
| Hidden imbalance below the root | `False` |
| Balanced tree that is not a BST | `True` |

Run the tests using:

```bash
python day_40_balanced_binary_tree.py
```

Expected test message:

```text
All tests passed!
```

## 8. Why the Algorithm Works

An empty subtree is balanced and has height `0`.

For every nonempty node:

- If either child subtree is unbalanced, the current subtree is unbalanced.
- If the child heights differ by more than `1`, the current subtree is unbalanced.
- Otherwise, the subtree is balanced and its height is `1 + max(left_height, right_height)`.

These conditions check the definition of height balance at every node.

## 9. Common Mistakes

| Mistake | Why it fails |
|---|---|
| Checking only the root | A lower subtree may be unbalanced |
| Comparing node counts | Balance depends on height |
| Requiring equal heights | A difference of `1` is allowed |
| Forgetting `abs()` | The difference must be nonnegative |
| Treating `-1` as a real height | It corrupts height calculations |
| Returning `bool(height)` | An empty balanced tree has height `0` |
| Assuming the function repairs the tree | It only checks balance |

A balanced binary tree does not necessarily have to be a Binary Search Tree (BST).

## 10. Complexity Analysis

Let `n` be the number of nodes and `h` be the height of the tree.

- **Time complexity:** `O(n)` in the worst case.
- **Auxiliary space:** `O(h)` for the recursive call stack.

A very deep tree may exceed Python's recursion limit.

## 11. Optional Extension

A helper can return a pair:

```python
(height, balanced)
```

This keeps the actual height separate from the boolean balance result and avoids using `-1` as a sentinel.

## 12. Key Learning

Height:

`1 + max(left_height, right_height)`

Balance condition:

`abs(left_height - right_height) <= 1`

The algorithm checks whether a tree is balanced; it does not repair the tree.
