from typing import List
from solution import Solution, ListNode


def get_list_of_values(head: ListNode) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next

    return result


def test_solution():
    # head = [1,2,3,3,4,4,5]
    head = ListNode(1)
    a = ListNode(2)
    b = ListNode(3)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(4)
    f = ListNode(5)

    head.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    expected = [1, 2, 5]
    result = Solution().deleteDuplicates(head)
    assert expected == get_list_of_values(result)
