# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ = 0
        def summa(tree, low, high):
            nonlocal summ
            if not tree:
                return
            if low <= tree.val <= high:
                summ += tree.val
            summa(tree.right, low, high)
            summa(tree.left, low, high)
            return summ
        return summa(root, low, high)