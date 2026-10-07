class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_depth(root):
    # Base case: empty subtree
    if root is None:
        return 0

    # Solve the two smaller subproblems
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # Count the current node
    return 1 + max(left_depth, right_depth)

root = TreeNode(
    3,
    left=TreeNode(9),
    right=TreeNode(
        20,
        left=TreeNode(15),
        right=TreeNode(7),
    ),
)

print(max_depth(root))