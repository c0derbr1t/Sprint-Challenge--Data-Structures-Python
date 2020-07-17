class RingBuffer: 
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None]*capacity 
    

    def append(self, thing): 
        self.storage[self.count] = thing
        self.count += 1 
        if self.count == self.capacity:
            self.count = 0

    def get(self): 
        return [thing for thing in self.storage if thing is not None]

"""
* Check understanding
"""
    # 8 items
    # capacity is 6
    # Find the final 0th index
        # 7!
"""
    1 -> 0 
    2 -> 1
    3 -> 2
    4 -> 3
    5 -> 4
    6 -> 5
    7 -> 0
    8 -> 1
"""