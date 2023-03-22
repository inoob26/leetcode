from solution import Solution, TreeNode


def test_solution():
    # root = [4,2,7,1,3],
    root = TreeNode(4)
    a = TreeNode(2)
    b = TreeNode(7)
    c = TreeNode(1)
    d = TreeNode(3)

    root.left = a
    root.right = b
    a.left = c
    a.right = d

    val = 2
    expected = a
    result = Solution().searchBST(root, val)
    assert expected == result
