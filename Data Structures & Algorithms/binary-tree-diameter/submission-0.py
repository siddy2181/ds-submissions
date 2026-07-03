# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0    
      # calculate height of left and right from the current node
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

      # add left and right to check diameter
            self.result = max(self.result, left+right)
            return 1+ max(left,right)
      # return the current max result
        dfs(root)
        return self.result

