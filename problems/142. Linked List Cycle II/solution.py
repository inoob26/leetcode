from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_map = set()
        itr = head
        while itr:
            if itr in head_map:
                return itr

            head_map.add(itr)
            itr = itr.next

        return None
