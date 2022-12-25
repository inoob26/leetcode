from solution import build_tree, Solution
import collections


def test_reverse():
    elements = [4, 2, 7, 1, 3, 6, 9]
    b_tree = build_tree(elements)

    expected = [4, 7, 9, 6, 2, 3, 1]
    reversed = Solution().invertTree(b_tree)
    pre_order = reversed.pre_order_traversal()

    assert expected == pre_order
