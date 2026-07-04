# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result= []
        q=collections.deque()
        q.append(root)

        while q:
            q_Length = len(q);
            temp = []
            for i in range(q_Length):
                curr=q.popleft()
                if curr:
                    temp.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if temp:
                result.append(temp)
        return result

