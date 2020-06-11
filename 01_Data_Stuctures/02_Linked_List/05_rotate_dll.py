class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class LinkedList:
	def __init__(self):
		self.head = None

def update(llist, p):
	current_node = llist.head
	current_tail = current_node
	while current_tail.next:
		current_tail = current_tail.next
	for i in range(p):
		current_tail.next = current_node
		current_node.prev = current_tail
		current_node = current_node.next
		current_tail = current_tail.next
	current_node.prev = None
	current_tail.next = None
	llist.head = current_node
	return llist

if __name__=="__main__":
	t = int(input())
	while t>0:
		liston = [int(x) for x in input().strip().split()]
		n = liston[0]
		p = liston[1]
		listto = [int(x) for x in input().strip().split()]
		llist = LinkedList()
		for i in range(n):
			ptr = Node(listto[i])
			if llist.head == None:
				llist.head = ptr
				cur = ptr
			else:
				cur.next = ptr
				ptr.prev = cur
				cur = ptr 

		New = update(llist, p)
		temp = New.head
		while temp:
			print(temp.data, end= " ")
			temp = temp.next
		print(" ")
		t = t-1
