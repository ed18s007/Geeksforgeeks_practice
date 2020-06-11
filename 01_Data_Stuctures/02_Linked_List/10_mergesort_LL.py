def merge(inp_list_1, inp_list_2):
	idx1, idx2 = 0, 0
	merge_list = []
	len1, len2 = len(inp_list_1), len(inp_list_2)
	for i in range(len1+len2):
		if inp_list_1[idx1] < inp_list_2[idx2]:
			merge_list.append(inp_list_1[idx1])
			idx1 += 1
			if idx1 == len1:
				merge_list.extend(inp_list_2[idx2:])
				return merge_list
		else:
			merge_list.append(inp_list_2[idx2])
			idx2 += 1
			if idx2 == len2:
				merge_list.extend(inp_list_1[idx1:])
				return merge_list
	return merge_list

def mergesort(inp_list):
	if len(inp_list) <=1:
		return inp_list
	mid = len(inp_list)//2
	low = mergesort(inp_list[:mid])
	high = mergesort(inp_list[mid:])
	return merge(low, high)

print(mergesort([1,4,2,5,8,3,0]))
