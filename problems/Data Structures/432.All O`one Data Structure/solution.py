# v2
class Block:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.keys = set()
        self.next = None
        self.prev = None

    def insert_after(self, new_block):
        old_next = self.next
        self.next = new_block
        new_block.prev = self
        new_block.next = old_next

        old_next.prev = new_block

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.next, self.prev = None, None


class AllOne:
    def __init__(self):
        self.head = Block()
        self.tail = Block()
        self.hash_map = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        # find current block
        if not key in self.hash_map:
            # take head block as current
            current_block = self.head
        else:
            # get block from map
            current_block = self.hash_map[key]
            current_block.keys.remove(key)

        # insert new block
        if current_block.val + 1 != current_block.next.val:
            new_block = Block(current_block.val + 1)
            current_block.insert_after(new_block)
        else:
            new_block = current_block.next

        new_block.keys.add(key)
        self.hash_map[key] = new_block

        if not current_block.keys and current_block.val != 0:
            current_block.remove()

    def dec(self, key: str) -> None:
        if not key in self.hash_map:
            return
        current_block = self.hash_map[key]
        del self.hash_map[key]
        current_block.keys.remove(key)

        if current_block.val != 1:
            # new block
            if current_block.val - 1 != current_block.prev.val:
                new_block = Block(current_block.val - 1)
                current_block.prev.insert_after(new_block)
            else:
                new_block = current_block.prev

            new_block.keys.add(key)
            self.hash_map[key] = new_block

        if not current_block.keys:
            current_block.remove()

    def getMaxKey(self) -> str:
        if self.tail.prev.val == 0:
            return ""

        key = self.tail.prev.keys.pop()
        self.tail.prev.keys.add(key)
        return key

    def getMinKey(self) -> str:
        if self.head.next.val == 0:
            return ""
        key = self.head.next.keys.pop()
        self.head.next.keys.add(key)
        return key


# v1
# class AllOne:

#     def __init__(self):
#         self.key_map = {}
#         self.max_key = ""
#         self.min_key = ""

#     def _update_min(self, key: int) -> None:
#         if not self.min_key: self.min_key = key
#         if self.max_key != key and self.key_map[key] <= self.key_map.get(self.min_key, -1):
#             self.min_key = key

#     def _update_max(self, key: int) -> None:
#         if not self.max_key:
#             self.max_key = key
#         if self.min_key != key and self.key_map[key] >= self.key_map.get(self.max_key, float("inf")):
#             self.max_key = key

#     def _remove_key(self, key: int) -> None:
#         if self._is_empty(): return

#         if key == self.max_key:
#             max_val = float("-inf")
#             for k, v in self.key_map.items():
#                 if v > max_val and k != key:
#                     max_val = v
#                     self.max_key = k
#         elif key == self.min_key:
#             min_val = float("inf")
#             for k, v in self.key_map.items():
#                 if v < min_val and k != key:
#                     min_val = v
#                     self.min_key = k

#         del self.key_map[key]


#     def inc(self, key: str) -> None:
#         if key in self.key_map:
#             self.key_map[key] += 1
#             self._update_max(key)
#             return

#         self.key_map[key] = 1
#         self._update_max(key)
#         self._update_min(key)

#     def dec(self, key: str) -> None:
#         if key in self.key_map:
#             self.key_map[key] -= 1
#             if self.key_map[key] == 0:
#                 self._remove_key(key)
#                 return
#             self._update_min(key)


#     def getMaxKey(self) -> str:
#         if self._is_empty(): return ""
#         return self.max_key

#     def getMinKey(self) -> str:
#         if self._is_empty(): return ""
#         return self.min_key

#     def _is_empty(self) -> bool:
#         return len(self.key_map.values()) == 0

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
