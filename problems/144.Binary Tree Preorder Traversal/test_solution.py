from solution import TreeNode, Solution


def test_solution():
    # root = [1,null,2,3]
    root = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)

    root.right = b
    b.left = c

    expected = [1, 2, 3]
    result = Solution().preorderTraversal(root)
    assert expected == result

    root = None
    expected = []
    result = Solution().preorderTraversal(root)
    assert expected == result

    root = TreeNode(1)
    expected = [1]
    result = Solution().preorderTraversal(root)
    assert expected == result
