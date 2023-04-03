from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode()
        node = result
        l1_node = l1
        l2_node = l2
        carry = 0
        while l1_node or l2_node or carry:
            l1_val = l1_node.val if l1_node else 0
            l2_val = l2_node.val if l2_node else 0
            val = l1_val + l2_val + carry

            carry = val // 10
            node.val = val % 10
            if (l1_node and l1_node.next) or (l2_node and l2_node.next) or carry:
                node.next = ListNode()
                node = node.next

            l1_node = l1_node.next
            l2_node = l2_node.next

        return result
