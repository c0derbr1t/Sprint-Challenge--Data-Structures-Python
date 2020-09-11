class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.count] = item
        self.count += 1
        
        if self.count == self.capacity:
            self.count = 0

    def get(self):
        return [item for item in self.storage if item is not None]