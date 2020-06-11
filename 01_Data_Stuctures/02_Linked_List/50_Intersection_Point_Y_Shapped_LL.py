 # Intersection Point in Y Shapped Linked Lists 

def intersetPoint(head_a,head_b):
    #code here
    curr_a = head_a
    curr_b = head_b
    num_a, num_b = 0, 0
    while curr_a:
        curr_a = curr_a.next
        num_a += 1
    while curr_b:
        curr_b = curr_b.next
        num_b += 1
    d = num_a - num_b
    curr_a, curr_b = head_a, head_b
    if d>0:
        while d>0:
            curr_a = curr_a.next
            d-=1
    else:
        d = abs(d)
        while d>0:
            curr_b = curr_b.next
            d-=1
    while not (curr_a== curr_b):
        curr_a = curr_a.next
        curr_b = curr_b.next
    return curr_a if curr_a is not None else -1

