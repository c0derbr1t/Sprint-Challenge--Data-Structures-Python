from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)

            else:
                self.left.insert(value)

        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)

            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True

        elif target < self.value:
            if self.left is None:
                return False

            else:
                return self.left.contains(target)

        elif target > self.value:
            if self.right is None:
                return False

            else:
                return self.right.contains(target)

    def get_max(self):
        max_value = self.value

        if self.right is None:
            return max_value

        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)

        if self.left is not None:
            self.left.for_each(cb)

        if self.right is not None:
            self.right.for_each(cb)

    def in_order_print(self, node):
        if self is None:
            return
        
        if self.left is not None:
            self.left.in_order_print(node)

        print(self.value)

        if self.right is not None:
            self.right.in_order_print(node)

    def bft_print(self, node):
        bft_queue = Queue()
        bft_queue.enqueue(self)

        while bft_queue.__len__() > 0:
            dequeued = bft_queue.dequeue()
            print(dequeued.value)

            if dequeued.left is not None:
                bft_queue.enqueue(dequeued.left)

            if dequeued.right is not None:
                bft_queue.enqueue(dequeued.right)

    def dft_print(self, node):
        dft_stack = Stack()
        dft_stack.push(self)

        while len(dft_stack) > 0:
            pop_node = dft_stack.pop()
            print(pop_node.value)

            if pop_node.left is not None:
                dft_stack.push(pop_node.left)

            if pop_node.right is not None:
                dft_stack.push(pop_node.right)

    def pre_order_dft(self, node):
        if node is None:
            return

        print(node.value)

        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    def post_order_dft(self, node):
        if node is None:
            return

        self.post_order_dft(node.left)
        self.post_order_dft(node.right)

        print(node.value)
    