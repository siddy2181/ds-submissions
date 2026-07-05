# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not (root.left or root.right): return 1
        def dfs(curr, maxVal):
            if not curr: return 0
            if curr.val >= maxVal: 
                maxVal = curr.val
                result =1
            else:
                result = 0
            result += dfs(curr.left, maxVal)
            result += dfs(curr.right, maxVal)
            return result
        return dfs(root, root.val);
            