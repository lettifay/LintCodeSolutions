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