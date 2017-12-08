# 366. Fibonacci
def fibonacci(n):
	a=0
	b=1
	while(n-1):
	    a,b=b,a+b
	    n=n-1
	return a

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

# 454. Rectangle Area
class Rectangle:

    #Define a constructor which expects two parameters width and height here.
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    #Define a public method 'getArea()' which can calculate the area of the rectangle and return.
    def getArea(self):
        return self.width*self.height

#  463. Sort Integers
def sortArray(A):
    for i in range(len(A)):
        for j in range(len(A[i:])):
            if A[i] > A[i+j]:
                A[i],A[i+j] = A[i+j],A[i]
    return A

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

# 632. Binary Tree Maximum Node
def maxNode(self, root):
        if root == None:
            return None
            
        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        
        sub_max = self.max(left,right)
        max = self.max(root,sub_max)
        
        return max
    
def max(self,a,b):
    if a == None:
        return b
    if b == None:
        return a
    if a.val > b.val:
        return a
    return b