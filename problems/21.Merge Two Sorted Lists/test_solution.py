from solution import Solution, ListNode


def _linkedlist_to_list(linked_list: ListNode):
    result = []

    while linked_list:
        result.append(linked_list.val)
        linked_list = linked_list.next

    return result


def test_solution():
    node3_1 = ListNode(4, None)
    node2_1 = ListNode(2, node3_1)
    node1_1 = ListNode(1, node2_1)

    node3_2 = ListNode(4, None)
    node2_2 = ListNode(3, node3_2)
    node1_2 = ListNode(1, node2_2)

    ex_node6 = ListNode(4, None)
    ex_node5 = ListNode(4, ex_node6)
    ex_node4 = ListNode(3, ex_node5)
    ex_node3 = ListNode(2, ex_node4)
    ex_node2 = ListNode(1, ex_node3)
    ex_node1 = ListNode(1, ex_node2)

    expected = _linkedlist_to_list(ex_node1)
    result = _linkedlist_to_list(Solution().mergeTwoLists(node1_1, node1_2))
    assert expected == result
