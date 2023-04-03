from typing import List
from solution import Solution, ListNode


def get_values_from_linkedlist(head: ListNode) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next

    return result


def test_solution():
    # l1 = [2,4,3], l2 = [5,6,4]
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # [7,0,8]
    expected = ListNode(7)
    expected.next = ListNode(0)
    expected.next.next = ListNode(8)

    result = Solution().addTwoNumbers(l1, l2)
    assert get_values_from_linkedlist(expected) == get_values_from_linkedlist(result)
