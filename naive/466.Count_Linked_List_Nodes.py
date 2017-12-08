# 466. Count Linked List Nodes
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def countNodes(head):
    if head == None:
        return 0
    
    count = 1
    check_node = head
    while (check_node.next != None):
        check_node = check_node.next
        count = count + 1
    return count