from solution import TreeNode, Solution


def test_solution():
    # root = [6,2,8,0,4,7,9,null,null,3,5]
    # p = 2
    # q = 8
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    p = TreeNode(2)
    q = TreeNode(8)
    expected = root.val
    result = Solution().lowestCommonAncestor(root, p, q)
    assert result.val == expected

    # root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    p = TreeNode(2)
    q = TreeNode(4)
    expected = root.left.val
    result = Solution().lowestCommonAncestor(root, p, q)
    assert result.val == expected

    root = TreeNode(2)
    root.left = TreeNode(1)
    p = TreeNode(2)
    q = TreeNode(1)
    expected = root.val
    result = Solution().lowestCommonAncestor(root, p, q)
    assert result.val == expected
