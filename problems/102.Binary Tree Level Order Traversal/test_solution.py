from solution import TreeNode, Solution


def test_solution():
    # root = [3,9,20,null,null,15,7]
    root = TreeNode(3)
    a = TreeNode(9)
    b = TreeNode(20)
    c = TreeNode(15)
    d = TreeNode(7)

    root.left = a
    root.right = b
    b.left = c
    b.right = d

    expected = [[3], [9, 20], [15, 7]]
    result = Solution().levelOrder(root)
    assert expected == result
