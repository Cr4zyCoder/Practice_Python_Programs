def minValue(node): 
    current = node
    while(current.left is not None):
        current = current.left
    return current

def deleteNode(root, key):
    
    if root is None:
        return root
    if key< root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        