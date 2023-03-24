from solution import TreeNode, Solution


def test_solution_true():
    # root = [5,3,6,2,4,null,7],
    k = 9
    root = TreeNode(5)
    a = TreeNode(3)
    b = TreeNode(6)
    c = TreeNode(2)
    d = TreeNode(4)
    e = TreeNode(7)

    root.left = a
    root.right = b
    a.left = c
    b.right = d

    b.right = e
    expected = True
    result = Solution().findTarget(root, k)
    assert expected == result


def test_solution_false():
    k = 28
    root = TreeNode(5)
    a = TreeNode(3)
    b = TreeNode(6)
    c = TreeNode(2)
    d = TreeNode(4)
    e = TreeNode(7)

    root.left = a
    root.right = b
    a.left = c
    b.right = d
    b.right = e

    expected = False
    result = Solution().findTarget(root, k)
    assert expected == result
