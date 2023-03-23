from solution import TreeNode, Solution


def test_solution():
    # root = [4,2,7,1,3],
    val = 5
    root = TreeNode(4)
    a = TreeNode(2)
    b = TreeNode(7)
    c = TreeNode(1)
    d = TreeNode(3)
    e = TreeNode(5)

    root.left = a
    root.right = b
    a.left = c
    a.right = d

    result = Solution().insertIntoBST(root, val)
    b.left = e
    expected = root
    assert expected == result

    # root = [40,20,60,10,30,50,70], val = 25
    root = TreeNode(40)
    a = TreeNode(20)
    b = TreeNode(60)
    c = TreeNode(10)
    d = TreeNode(30)
    e = TreeNode(50)
    f = TreeNode(70)
    g = TreeNode(25)

    root.left = a
    root.right = b
    a.left = c
    a.right = d
    b.left = e
    b.right = f

    result = Solution().insertIntoBST(root, val)
    d.left = g
    expected = root
    assert expected == result
