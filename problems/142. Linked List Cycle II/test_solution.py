from solution import Solution, ListNode


def test_solution():
    # [3,2,0,-4]
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next

    expected = head.next
    result = Solution().detectCycle(head)
    assert result == expected

    head = ListNode(1)
    expected = None
    result = Solution().detectCycle(head)
    assert result == expected
