from solution import TreeNode, Solution


def test_solution():
    # root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
    root = TreeNode(5)
    a = TreeNode(4)
    b = TreeNode(8)
    c = TreeNode(11)
    d = TreeNode(7)
    e = TreeNode(2)
    f = TreeNode(13)
    g = TreeNode(4)
    h = TreeNode(1)

    root.left = a
    root.right = b

    a.left = c
    b.left = f
    b.right = g
    g.right = h

    c.left = d
    c.right = e

    targetSum = 22
    expected = True
    result = Solution().hasPathSum(root, targetSum)
    assert expected == result
