# implementation with DLinkedList
class DLinkedList:
    def __init__(self, val=0, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularDeque:
    def __init__(self, k: int):
        self.capacity: int = k
        self.size: int = 0
        self.head = None
        self.last = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = DLinkedList(value)
        if not self.head:
            self.head = new_node
            self.last = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = DLinkedList(value)
        if not self.head:
            self.head = new_node
            self.last = self.head
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        if not self.head.next:
            self.last = self.head = None
        else:
            next_node = self.head.next
            next_node.prev = None
            self.head.next = None
            self.head = next_node

        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if not self.last.prev:
            self.last = self.head = None
        else:
            prev_node = self.last.prev
            prev_node.next = None
            self.last.prev = None
            self.last = prev_node

        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head.val if self.head else -1

    def getRear(self) -> int:
        return self.last.val if self.last else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# implementation with List
# class MyCircularDeque:
#     def __init__(self, k: int):
#         self.capacity = k
#         self.size = 0
#         self.queue = []

#     def insertFront(self, value: int) -> bool:
#         if self.size == self.capacity:
#             return False

#         self.queue.insert(0, value)
#         self.size += 1
#         return True

#     def insertLast(self, value: int) -> bool:
#         if self.size == self.capacity:
#             return False

#         self.queue.append(value)
#         self.size += 1
#         return True

#     def deleteFront(self) -> bool:
#         if self.isEmpty():
#             return False

#         del self.queue[0]
#         self.size -= 1
#         return True

#     def deleteLast(self) -> bool:
#         if self.isEmpty():
#             return False

#         del self.queue[-1]
#         self.size -= 1
#         return True

#     def getFront(self) -> int:
#         if self.isEmpty():
#             return -1

#         return self.queue[0]

#     def getRear(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[-1]

#     def isEmpty(self) -> bool:
#         return self.size == 0

#     def isFull(self) -> bool:
#         return self.size == self.capacity
