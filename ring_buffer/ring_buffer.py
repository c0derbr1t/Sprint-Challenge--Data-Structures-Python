class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0
        self.oldest = None
        self.store = []

    def __len__(self):
        return self.size

    def __is_empty(self):
        return self.size == 0

    def __is_full(self):
        return self.size == self.capacity

    def append(self, item):
        if self.__is_empty():
            new_node = Node(item)
            self.head = new_node
            self.tail = new_node
            self.oldest = new_node
            self.size = 1
        elif not self.__is_full():
            current_tail = self.tail
            new_node = Node(item, prev_node=self.oldest, next_node=None)
            self.tail = new_node
            current_tail.next_node = self.tail
            self.size +=1
        elif self.__is_full():
            current_oldest = self.oldest
            if current_oldest == self.head:
                self.oldest = current_oldest.next_node
                new_node = Node(item, prev_node=None, next_node=self.oldest)
                self.head = new_node
            elif current_oldest == self.tail:
                self.oldest = self.head
                new_node = Node(item, prev_node=current_oldest.prev_node, next_node=None)
                self.tail = new_node
            else:
                self.oldest = current_oldest.next_node
                new_node = Node(item, prev_node=current_oldest.prev_node, next_node=self.oldest)

    def get(self):
        self.store.append(self.head.value)
        add = self.head.next_node
        while len(self.store) != self.capacity:
            self.store.append(add.value)
            add = add.next_node