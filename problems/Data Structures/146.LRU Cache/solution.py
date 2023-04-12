class DLinkedNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.size = 0
        self.head = DLinkedNode()
        self.tail = DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: DLinkedNode):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _move_node_to_head(self, node: DLinkedNode):
        self._remove_node(node)
        self._add_node(node)

    def _remove_node(self, node: DLinkedNode):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _pop_tail(self) -> DLinkedNode:
        node = self.tail.prev
        self._remove_node(node)
        return node

    def put(self, key: int, value: int) -> None:
        if key not in self.hash_map:
            new_node = DLinkedNode()
            new_node.value = value
            new_node.key = key

            self.hash_map[key] = new_node
            self._add_node(new_node)
            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.hash_map[tail.key]
                self.size -= 1
        else:
            node = self.hash_map[key]
            node.value = value
            self._move_node_to_head(node)

    def get(self, key: int) -> int:
        node = self.hash_map.get(key)
        if not node:
            return -1

        self._move_node_to_head(node)
        return node.value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
