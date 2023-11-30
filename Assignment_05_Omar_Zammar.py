# class TreeNode:
#     def __init__(self, name, fam, birth):
#         self.name = name
#         self.fam = fam
#         self.birth = birth
#         self.left = None
#         self.right = None
#
#
# class Tree:
#     def __init__(self, root, name, fam, birth):
#         self.root = TreeNode(root,name,fam)
#
#
# tree = Tree(1,"omar","zizi",12)
# tree.root.left = TreeNode(4,"omar","zamm")
# tree.root.right = TreeNode(7,"ali","we")
# tree.root.left.left = TreeNode(2,"eoo","erw")
# tree.root.left.right = TreeNode(5,"anas","janitor")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

# Example usage:
#      1
#     / \
#    2   3
#   / \
#  4   5

tree = BinaryTree(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)

print(tree.root)






