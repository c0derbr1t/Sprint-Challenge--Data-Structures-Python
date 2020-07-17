class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def print_ll(self):
        current = self.head
        if current != None:
            print(current.value)
            current = current.next_node

    def reverse_list(self, node, prev):
        if node == None:
            return node
        if node.next_node == None:
            return node

        current = node.next
        next = node.next_node
        if node == None:
            self.head = current
            print(current.value)
        else:
            self.reverse_list(next, current)
        # if not self.head:
        #     return
        # if not self.head.next_node:
        #     return self.head.value
        # if self.head.next_node:
        #     if current.next_node == None:
        #         self.add_to_head(current)
        #     else:
        #         current = current.next_node
        #         self.reverse_list(node, prev)
    
            
mine = LinkedList()
mine.add_to_head(1)
mine.print_ll()
mine.add_to_head(2)
mine.print_ll()
mine.add_to_head(3)
mine.print_ll()
mine.add_to_head(4)
mine.print_ll()
mine.add_to_head(5)
mine.print_ll()
print('\n-------------\n')
mine.reverse_list(mine.head, None)

