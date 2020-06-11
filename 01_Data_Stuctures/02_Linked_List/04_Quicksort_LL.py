from collections import defaultdict

def quicksort(input_list):
	if len(input_list) <=1:
		return input_list

	elif len(input_list) == 2:
		if input_list[0] <= input_list[1]:
			return input_list
		else:
			return input_list[::-1]

	pivot_idx = len(input_list) - 1
	swap_idx = 0
	while swap_idx < pivot_idx:
		if input_list[swap_idx] > input_list[pivot_idx]:
			input_list[swap_idx], input_list[pivot_idx - 1], input_list[pivot_idx] = input_list[pivot_idx - 1], input_list[pivot_idx], input_list[swap_idx]
			pivot_idx -= 1
		else:
			swap_idx += 1

	return quicksort(input_list[:pivot_idx]) + quicksort(input_list[pivot_idx:])


def partition(arr, low, high):
	i = low-1
	pivot = arr[high]

	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1

def quickSort(arr, low, high):
	if low < high:
		pi = partition(arr, low, high)

		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

arr = [6,2,4,1]
quickSort(arr, 0, 3)
print(arr)

def quicksort_ll(current_node):
	if current_node is None:
		return None
	if current_node.next is None:
		return current_node
	if current_node.next.next is None:
		if current_node.data <= current_node.next.data:
			return current_node
		else:
			val = current_node.data
			current_node.data = current_node.next.data
			current_node.next.data = val
			return current_node
	
	dic = defaultdict(list)
	nodeID(current_node, dic)
	
	swap_node = current_node
	tmp_node = current_node.next
	prev_node = current_node
	while tmp_node:
		pivot_node = tmp_node
		prev_node = prev_node.next
		tmp_node = tmp_node.next 

	while swap_node != pivot_node:
		if swap_node.data > pivot_node


		if input_list[swap_idx] > input_list[pivot_idx]:
			input_list[swap_idx], input_list[pivot_idx - 1], input_list[pivot_idx] = input_list[pivot_idx - 1], input_list[pivot_idx], input_list[swap_idx]
			pivot_idx -= 1
		else:
			swap_idx += 1

"""
class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class Llist:
	def __init__(self):
		self.head = None

	def insert(self, data, tail):
		node = Node(data)

		if not self.head:
			self.head = node
			return node

		tail.next = node 
		return node

def nodeID(head, dic):
	while head:
		dic[head.data].append(id(head))
		head = head.next

def printList(head, dic):
	while head:
		if id(head) not in dic[head.data]:
			print("Don't swap data, swap node")
			return
		print(head.data, end=" ")
		head = head.next



if __name__ == "__main__":
	t = int(input())

	for tcs in range(t):
		n=int(input())
		arr = [int(x) for x in input().split()]

		ll = Llist()
		tail = None

		for nodeData in arr:
			tail = ll.insert(nodeData, tail)

		dic = defaultdict(list)
		nodeID(ll.head, dic)

		resHead = quicksort_ll(ll.head)
		printList(resHead, dic)
		print()


"""