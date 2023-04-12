class CustomStack:
    def __init__(self, maxSize: int):
        self.capacity = maxSize
        self.size = 0
        self.stack = []

    def push(self, x: int) -> None:
        if self.size != self.capacity:
            self.stack.append(x)
            self.size += 1

    def pop(self) -> int:
        if self.stack:
            self.size -= 1
            return self.stack.pop()
        return -1

    def _increment_values(self, start: int, end: int, step: int, val: int):
        for indx in range(start, end, step):
            self.stack[indx] += val

    def increment(self, k: int, val: int) -> None:
        if k <= self.size:
            self._increment_values(start=0, end=k, step=1, val=val)
        else:
            self._increment_values(start=0, end=self.size, step=1, val=val)


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
