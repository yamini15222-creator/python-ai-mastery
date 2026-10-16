
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def is_balanced(root):
   

    def checked_height(node):
        if node is None:
            return 0

        # Calculate left subtree height
        left_height = checked_height(node.left)

        # Stop if the left subtree is unbalanced
        if left_height == -1:
            return -1

        # Calculate right subtree height
        right_height = checked_height(node.right)

        # Stop if the right subtree is unbalanced
        if right_height == -1:
            return -1

        # Check the height difference at this node
        if abs(left_height - right_height) > 1:
            return -1

        # Return the valid height to the parent
        return 1 + max(left_height, right_height)

    return checked_height(root) != -1




def trace_balance(root):
    """Print postorder helper results for understanding."""

    rows = []

    def checked_height(node):
        if node is None:
            return 0

        left_height = checked_height(node.left)

        # Failure travels upward immediately
        if left_height == -1:
            rows.append((node.value, left_height, "-", "-", -1))
            return -1

        right_height = checked_height(node.right)

        if right_height == -1:
            rows.append((node.value, left_height, right_height, "-", -1))
            return -1

        difference = abs(left_height - right_height)

        if difference > 1:
            rows.append((
                node.value,
                left_height,
                right_height,
                difference,
                -1
            ))
            return -1

        result = 1 + max(left_height, right_height)

        rows.append((
            node.value,
            left_height,
            right_height,
            difference,
            result
        ))

        return result

    result = checked_height(root)

    print("\nPOSTORDER DRY RUN")
    print("-" * 60)
    print(
        f"{'Node':<8}{'Left H':<10}{'Right H':<11}"
        f"{'Difference':<13}{'Returns':<10}"
    )
    print("-" * 60)

    for row in rows:
        print(
            f"{row[0]:<8}{row[1]!s:<10}"
            f"{row[2]!s:<11}{row[3]!s:<13}"
            f"{row[4]!s:<10}"
        )

    print("-" * 60)
    print("Final result:", result != -1)

    return result != -1



#          10
#         /  \
#        4    20
#       / \     \
#      2   6     30
#         /
#        5
#
# Expected: True


def build_tree_a():
    return TreeNode(
        10,
        left=TreeNode(
            4,
            left=TreeNode(2),
            right=TreeNode(
                6,
                left=TreeNode(5)
            )
        ),
        right=TreeNode(
            20,
            right=TreeNode(30)
        )
    )




#          10
#         /  \
#        4    20
#       / \     \
#      2   6     30
#         /
#        5
#       /
#      7
#
# Expected: False
# Node 6 is the first node to detect imbalance
# during the left-first traversal.


def build_tree_b():
    return TreeNode(
        10,
        left=TreeNode(
            4,
            left=TreeNode(2),
            right=TreeNode(
                6,
                left=TreeNode(
                    5,
                    left=TreeNode(7)
                )
            )
        ),
        right=TreeNode(
            20,
            right=TreeNode(30)
        )
    )




def height_and_balance(root):
   

    if root is None:
        return 0, True

    left_height, left_balanced = height_and_balance(root.left)
    right_height, right_balanced = height_and_balance(root.right)

    height = 1 + max(left_height, right_height)

    balanced = (
        left_balanced
        and right_balanced
        and abs(left_height - right_height) <= 1
    )

    return height, balanced




def run_tests():
   
    assert is_balanced(None) is True

    
    assert is_balanced(TreeNode(10)) is True

   
    assert is_balanced(
        TreeNode(1, left=TreeNode(2))
    ) is True

    
    balanced_tree = TreeNode(
        1,
        TreeNode(2, left=TreeNode(4)),
        TreeNode(3)
    )
    assert is_balanced(balanced_tree) is True

   
    unbalanced_tree = TreeNode(
        1,
        left=TreeNode(
            2,
            left=TreeNode(3)
        )
    )
    assert is_balanced(unbalanced_tree) is False

   
    tree_a = build_tree_a()
    assert is_balanced(tree_a) is True

   
    tree_b = build_tree_b()
    assert is_balanced(tree_b) is False

    
    hidden_imbalance = TreeNode(
        1,
        TreeNode(
            2,
            left=TreeNode(
                4,
                left=TreeNode(6)
            )
        ),
        TreeNode(
            3,
            right=TreeNode(
                5,
                right=TreeNode(7)
            )
        )
    )
    assert is_balanced(hidden_imbalance) is False

    
    not_a_bst = TreeNode(
        1,
        TreeNode(9),
        TreeNode(2)
    )
    assert is_balanced(not_a_bst) is True

    
    duplicates = TreeNode(
        5,
        TreeNode(5),
        TreeNode(5)
    )
    assert is_balanced(duplicates) is True

    
    assert height_and_balance(None) == (0, True)
    assert height_and_balance(tree_a)[1] is True
    assert height_and_balance(tree_b)[1] is False

    before = tree_snapshot(tree_a)
    is_balanced(tree_a)
    after = tree_snapshot(tree_a)
    assert before == after

    print("All tests passed!")




def tree_snapshot(node):
    if node is None:
        return None

    return (
        node.value,
        tree_snapshot(node.left),
        tree_snapshot(node.right)
    )




def print_learning_notes():
    print("\nKEY CONCEPTS")
    print("1. Height = 1 + max(left_height, right_height)")
    print("2. Balance requires abs(left_height - right_height) <= 1")
    print("3. Both child subtrees must also be balanced.")
    print("4. -1 means unbalanced, not a real height.")
    print("5. This function checks balance; it does not repair the tree.")
    print("6. Balanced does not necessarily mean a valid BST.")

    print("\nCOMPLEXITY")
    print("Time: O(n) in the worst case")
    print("Auxiliary space: O(h) for recursive calls")




if __name__ == "__main__":

    run_tests()

    
    tree_a = build_tree_a()
    print("\n TREE A")
    print("Expected: True")
    print("Actual:", is_balanced(tree_a))
    trace_balance(tree_a)

    
    tree_b = build_tree_b()
    print("\n TREE B")
    print("Expected: False")
    print("Actual:", is_balanced(tree_b))
    trace_balance(tree_b)

   
    height, balanced = height_and_balance(tree_a)
    print("\nOPTIONAL EXTENSION")
    print("Tree A height:", height)
    print("Tree A balanced:", balanced)

    
    print_learning_notes()
