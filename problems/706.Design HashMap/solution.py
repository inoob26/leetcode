# v2
class Bucket:
    def __init__(self):
        self._bucket = []

    def get(self, key: int) -> int:
        for k, value in self._bucket:
            if k == key:
                return value
        return -1

    def update(self, key: int, value: int) -> None:
        found = False
        for indx, key_val in enumerate(self._bucket):
            if key == key_val[0]:
                self._bucket[indx] = (key, value)
                found = True
                break
        if not found:
            self._bucket.append((key, value))

    def remove(self, key: int) -> None:
        for indx, key_val in enumerate(self._bucket):
            if key == key_val[0]:
                del self._bucket[indx]


class MyHashMap:
    def __init__(self):
        self._size = 1000
        self._hash_table = [Bucket() for _ in range(self._size)]

    def _hash_key(self, key: int) -> int:
        return key % self._size

    def put(self, key: int, value: int) -> None:
        self._hash_table[self._hash_key(key)].update(key, value)

    def get(self, key: int) -> int:
        return self._hash_table[self._hash_key(key)].get(key)

    def remove(self, key: int) -> None:
        self._hash_table[self._hash_key(key)].remove(key)


# v1 my solution
# class MyHashMap:
#     def __init__(self):
#         self._keys = []
#         self._values = []
#         dict()

#     def put(self, key: int, value: int) -> None:
#         if key not in self._keys:
#             self._keys.append(key)
#             self._values.append(value)
#             return
#         self._values[self._keys.index(key)] = value

#     def get(self, key: int) -> int:
#         if key not in self._keys:
#             return -1
#         return self._values[self._keys.index(key)]

#     def remove(self, key: int) -> None:
#         if key in self._keys:
#             self._values.pop(self._keys.index(key))
#             self._keys.remove(key)
