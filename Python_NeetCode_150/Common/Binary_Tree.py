class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(node):
    if node: print(f"Node value: {node.val}")
    print_tree(node.left)
    print_tree(node.right)

def create_tree_from_list(lst):
    if not lst:
        return None # so an empty list = false?
    
    root = TreeNode(lst[0]) # Initiating a tree node like this [1,2,3] would mean this is TreeNode(1). So this initiates a treenode with a val=1?
    queue = [root] # We create a variable called que, but it is not an actual que object, it is just a list of treenodes?
    i = 1

    while i < len(lst):
        current=queue.pop(0) # Assign root as current
        if lst[i] is not None: # Next item in array represents left node of root. Is there a left node?
            current.left = TreeNode(lst[i]) # Set currents left node to next item in list
            queue.append(current.left) # Append left node to que
        i += 1 # increment i to traverse the array

        if i < len(lst) and lst[i] is not None: # Next item in array represent right node of root. Is there a right node?
            current.right = TreeNode(lst[i]) # If so, assign the right node to the root
            queue.append(current.right) # Append left node to que
        i += 1 # increment i to traverse the array
