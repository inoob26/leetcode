from solution import TreeNode, Solution


def test_empty_root():
    root = None
    expected = True
    result = Solution().isBalanced(root)
    assert result == expected


def test_balanced():
    # root = [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    expected = True
    result = Solution().isBalanced(root)
    assert result == expected


test_balanced()
