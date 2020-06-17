 # Implement Stack using Linked List 
# Class to represent a node
class StackNode:

	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
    def __init__(self):
        self.head = StackNode(None)

    # The method push to push element into
    # the stack
    def push(self, data):

        # Add code here
        if self.head is None:
            self.head = StackNode(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = StackNode(data)

        # The method pop which return the element
        # poped out of the stack

    def pop(self):

        # Add code here
        if self.head is None:
            return None
        elif self.head.next.next is None:
            val = self.head.next.data
            self.head.next = None
            return None
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            val =current_node.next.data
            current_node.next = None
            return val