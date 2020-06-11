 # linked list of strings forms a palindrome 
def compute(head): 
    #return True/False
    curr_node = head
    string = ""
    while curr_node:
        string+=curr_node.data
        curr_node = curr_node.next
    n = len(string)
    if(n%2==0):
        frst, scnd = string[:n//2],string[n//2:]
    else:
        frst, scnd = string[:n//2],string[(n//2)+1:]
    if(frst==scnd[::-1]):
        return True
    else:
        return False