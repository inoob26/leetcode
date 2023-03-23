from solution import TreeNode, Solution


def test_solution():
    # root = [1,2,2,3,4,4,3]
    root = TreeNode(1)
    a = TreeNode(2)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(4)
    f = TreeNode(3)

    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.left = e
    b.right = f

    expeted = True
    result = Solution().isSymmetric(root)
    assert expeted == result
