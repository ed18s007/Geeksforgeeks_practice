class Node(object):
	def __init__(self,data):
		self.data = data
		self.right = None
		self.down = None

class LinkedList:
	def __init__(self):
		self.head = None

	def display(self):
		Dp = self.head
		while Dp:
			Rp = Dp
			while Rp:
				print(Rp.data, end=" ")
				Rp = Rp.right
			Dp = Dp.down
		print(" ")

def construct(arr, n):
	head_node = Node(arr[0][0])
	current_node = head_node
	for i in range(n):
		start_node = current_node
		for j in range(n):
			if j<n-1:
				current_node.right = Node(arr[i][j+1])
			if i<n-1:
				current_node.down = Node(arr[i+1][j])
			current_node = current_node.right
		if i < n-1:
			current_node = start_node.down
	return head_node

if __name__=="__main__":
	t = int(input())
	while(t>0):
		n = int(input())
		arr = [[0 for i in range(n)] for j in range(n)]
		listto = [int(x) for x in input().strip().split()]
		k = 0
		for i in range(n):
			for j in range(n):
				arr[i][j] = listto[k]
				k += 1
		llist = LinkedList()
		llist.head = construct(arr, n)
		llist.display()
		t -= 1
