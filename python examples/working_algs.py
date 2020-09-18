

def inorderTraversal(self, root):
    ans = []
    stack = []
    
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            ans.append(tmpNode.val)
            root = tmpNode.right
        
    return ans

def preorderTraversal(self,root):
    """
    while loop
        if the value exists
        add the node... add the left and right nodes
        stack pops off end... so add right then left (preorder is root->left-> right)
    
    """
    res = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res