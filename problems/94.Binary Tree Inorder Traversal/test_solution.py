from solution import TreeNode, Solution


def test_solution():
    # root = [1,null,2,3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    expected = [1, 3, 2]
    result = Solution().inorderTraversal(root)
    assert expected == result
