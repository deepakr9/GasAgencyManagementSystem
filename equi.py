class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tree 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)

# Tree 2
root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.right = TreeNode(2)
root2.right.right = TreeNode(4)
def flipEquiv( root1, root2):
        if root1 is None and root2 is None:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            return (flipEquiv(root1.left, root2.left) and flipEquiv(root1.right, root2.right) or flipEquiv(root1.left, root2.right) and flipEquiv(root1.right, root2.left))
        return False


print(flipEquiv(root1, root2))