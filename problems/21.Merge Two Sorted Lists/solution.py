from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2

        elif list2 is None:
            return list1

        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


# my bad approach =(
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = ListNode(data, None)
#             return

#         itr = self.head
#         while itr.next:
#             itr = itr.next

#         self.itr.next = ListNode(data, None)

#     def get_head():
#         return self.head


# class Solution:
#     def mergeTwoLists(
#         self, list1: Optional[ListNode], list2: Optional[ListNode]
#     ) -> Optional[ListNode]:
#         result = None
#         item_1 = None
#         item_2 = None
#         while list1 or list2:
#             if result is None:
#                 result = LinkedList()

#             if list1:
#                 item_1 = list1.val
#                 list1 = list1.next
#                 result.insert_at_end(item_1)

#             if list2:
#                 item_2 = list2.val
#                 list2 = list2.next
#                 result.insert_at_end(item_2)

#         return result.get_head()
