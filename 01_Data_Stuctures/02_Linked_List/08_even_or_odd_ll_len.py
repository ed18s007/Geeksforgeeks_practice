"""
int isLengthEvenOrOdd(struct Node* head)
{
     //Code here
     struct Node *current_node;
     current_node = head;
     int cnt = 0;
     while(current_node)
     {
         cnt = cnt+1;
         current_node = current_node->next;
     }
     cnt = cnt%2;
     return cnt;
}
"""
def isLengthEvenOrOdd(head):
    # Code here
    current_node = head
    cnt = 1
    while current_node:
        cnt += 1
        current_node = current_node.next
    
    return cnt%2