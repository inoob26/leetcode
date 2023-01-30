from solution import Solution, ListNode


def test_solution():
    head = ListNode(1, None)

    head.next = ListNode(2, None)
    head.next.next = ListNode(3, None)
    head.next.next.next = ListNode(4, None)
    head.next.next.next.next = ListNode(5, None)

    expected = [5, 4, 3, 2, 1]
    result = Solution().reverseList(head)
    res_lst = []
    while result:
        res_lst.append(result.val)
        result = result.next
    assert expected == res_lst
