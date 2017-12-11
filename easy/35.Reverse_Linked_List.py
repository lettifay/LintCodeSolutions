# 35. Reverse Linked List
def reverse(head):
    pre = None
    while(head != None):
        tmp = head.next
        head.next = pre
        pre = head
        head = tmp
    return pre