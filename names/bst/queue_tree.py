from .singly_linked_list_tree import LinkedList
from .stack_tree import Stack
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   * Using an array, you can used the built in insert and pop functions.
   * Using a linked list, you have to create the linked list, and set it to add and remove from opposite ends of the LL. Functionality on a small dataset it is about the same.
   * If you had a large dataset, the linked list might be better. You have no need to get to or use the middle values. The dequeued value is the important one. It's waited in line to be used through the whole queue since it was added at the beginning (from tail to head).
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# Implementation with *list*
class Queue_lst:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.insert(0, value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.pop()

# # Implemetation with *Linked List* where add to head, remove from tail....doesn't work!
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.add_to_head(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.remove_tail()

# # Implemetation with *Linked List* where add to tail, remove from head...and it WORKS.
class Queue:  # Queue_LL
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -=1
            return self.storage.remove_head()

"""
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# # Added a method to singly_linked_list_q.py
# class Queue_stk_attempt_2:
#     def __init__(self):
#         self.size = 0
#         self.storage = Stack_lst()

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.push(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size == 0:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop_first()
    
class Queue_stk_attempt_3:
    def __init__(self):
        self.size = 0
        self.storage = Stack()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.push(value)
        self.size += 1
        return self.storage

    def dequeue(self):
        if self.storage.__len__() == 0:
            return None
        elif self.storage.__len__() == 1:
            print("dequeue: " + str(self.storage.pop()))
            return self.storage.pop()
        else:
            temp_stack = Stack()
            while temp_stack.__len__() != self.size:
                popped = self.storage.pop()
                temp_stack.push(popped)
                if temp_stack.__len__() == 1:
                    self.size -= 1
                    print("dequeue: " + str(self.storage.pop()))
                    return self.storage.pop()

class Queue_stk_attempt_1:
    def __init__(self):
        self.size_1 = 0
        self.size_2 = 0
        self.storage_1 = Stack()
        self.storage_2 = Stack()

    def __len__(self):
        return self.size_1

    def enqueue(self, value):
        self.storage_1.push(value)
        self.size_1 += 1
        return self.storage_1

    def dequeue(self):
        if self.size_1 == 0:
            return None
        elif self.size_1 > 0:
            while self.size_1 != self.size_2 - 1:
                pop = self.storage_1.pop()
                self.storage_2.push(pop)
                self.size_2 += 1
            if self.size_1 == self.size_2 - 1:
                self.size_1 -= 1
                return self.storage_1.pop()

"""
For trying to build Queue_stk_attempt_1
a_queue = Queue_stk_attempt_1()

a_queue.enqueue("A")
a_queue.enqueue("B")
a_queue.enqueue("C")
a_queue.enqueue("D")
a_queue.enqueue("E")
a_queue.enqueue("F")
a_queue.enqueue("G")
a_queue.enqueue("H")
a_queue.enqueue("I")
a_queue.enqueue("J")
a_queue.enqueue("K")


a_queue.dequeue() # J
a_queue.dequeue() # G
a_queue.dequeue() # D
"""