from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.frequency_map = defaultdict(OrderedDict)
        self.lfu_cache = {}  # key: (freq, val)

    def insert(self, key: int, frequency: int, value: int):
        self.lfu_cache[key] = (frequency, value)
        self.frequency_map[frequency][key] = value

    def get(self, key: int) -> int:
        if key not in self.lfu_cache:
            return -1

        frequency, value = self.lfu_cache[key]
        del self.frequency_map[frequency][key]
        if self.min_freq == frequency and not self.frequency_map[frequency]:
            self.min_freq += 1
        self.insert(key, frequency + 1, value)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.lfu_cache:
            self.get(key)
            # update value
            self.lfu_cache[key] = (self.lfu_cache[key][0], value)
            return

        if self.capacity == len(self.lfu_cache):
            # remove least elem
            k, v = self.frequency_map[self.min_freq].popitem(last=False)
            del self.lfu_cache[k]

        # add new one
        self.min_freq = 1
        self.insert(key, self.min_freq, value)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
