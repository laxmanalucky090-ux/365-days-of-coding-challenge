class FrontMiddleBackQueue:
    def __init__(self):
        self.q = []

    def pushFront(self, val: int) -> None:
        self.q.insert(0, val)  # Insert at index 0

    def pushBack(self, val: int) -> None:
        self.q.append(val)  # Add at end

    def pushMiddle(self, val: int) -> None:
        mid = len(self.q) // 2  # middle index
        self.q.insert(mid, val)  # Insert at middle

    def popFront(self) -> int:
        if not self.q:
            return -1
        return self.q.pop(0)  # Remove first element

    def popBack(self) -> int:
        if not self.q:
            return -1
        return self.q.pop()  # Remove last element

    def popMiddle(self) -> int:
        if not self.q:
            return -1
        mid = (len(self.q) - 1) // 2  # frontmost middle
        return self.q.pop(mid)  # Remove middle element

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()