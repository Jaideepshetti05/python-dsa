class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))