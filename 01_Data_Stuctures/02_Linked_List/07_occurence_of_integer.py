"""
int count(struct node* head, int search_for)
{
int cnt=0;
struct node *current_node;
current_node = head;
while(current_node)
{
    if(current_node->data == search_for){
        cnt = cnt + 1;
    }
    current_node = current_node->next;
}
return cnt;
}
"""
def count(head, search_for):
    # Code here
    current_node = head
    cnt = 0
    while current_node:
        if current_node.data == search_for:
            cnt += 1
        current_node = current_node.next
    return cnt