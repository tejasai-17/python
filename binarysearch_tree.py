class BSTNode:
    def __init__(self, data):
        self.leftChild = None
        self.rightChild = None
        self.data = data

def insertNode(root_node, node_value):
    if root_node is None:  
        return BSTNode(node_value)

    if node_value < root_node.data:  
        root_node.leftChild = insertNode(root_node.leftChild, node_value)
    else:
        root_node.rightChild = insertNode(root_node.rightChild, node_value)

    return root_node  

def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current

def deleteNode(root_node, node_value):
    if root_node is None:
        print(node_value, "not found in the tree.")
        return None

    if node_value < root_node.data:
        root_node.leftChild = deleteNode(root_node.leftChild, node_value)

    elif node_value > root_node.data:
        root_node.rightChild = deleteNode(root_node.rightChild, node_value)

    else:
        if root_node.leftChild is None:
            temp = root_node.rightChild
            print("Element deleted successfully")
            return temp  

        if root_node.rightChild is None:
            temp = root_node.leftChild
            print("Element deleted successfully")
            return temp  

        temp = minValueNode(root_node.rightChild)  
        root_node.data = temp.data
        root_node.rightChild = deleteNode(root_node.rightChild, temp.data)  

    return root_node  

def inorderTraversal(root_node):
    if root_node is not None:
        inorderTraversal(root_node.leftChild)
        print(root_node.data, end=" ")
        inorderTraversal(root_node.rightChild)

root = None
root = insertNode(root, 50)
root = insertNode(root, 30)
root = insertNode(root, 70)
root = insertNode(root, 20)
root = insertNode(root, 40)
root = insertNode(root, 60)
root = insertNode(root, 80)

print("Inorder before deletion:")
inorderTraversal(root)
print("\n")

root = deleteNode(root, 50)

print("Inorder after deletion:")
inorderTraversal(root)
print()
