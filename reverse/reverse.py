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

    def reverse_list(self, node, prev):
        if node is None:
            return
        # when you hit the end of the linked list (node is at the end)
        if node.next_node is None:
            # make the next node the previous node instead
            node.next_node = prev
            # set the head of the LL at this end node
            self.head = node
            return
        else:
            # recursively call the function using the next node as the starting node
            # this will continue iterating through the LL until node.next_node is None
            self.reverse_list(node.next_node, node)
        # Make the next node the previous node
        node.next_node = prev