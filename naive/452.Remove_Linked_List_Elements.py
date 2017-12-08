# 452. Remove Linked List Elements
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeElements(head, val):
    if head == None:
        return None
    
    # create a new node before head, called 'new_node'
    new_node = ListNode(0)
    new_node.next = head
    
    # the new head of this singly-linked list change to the 'new_node'
    head = new_node
    
    # create a check_node to traversal every node
    check_node = head
    while (check_node.next != None):
        if check_node.next.val == val:
            check_node.next = check_node.next.next
        else:
            check_node = check_node.next
            
    return head.next