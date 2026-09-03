# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        ans = []

        def inorder(node):
            if node is None:
                return None

            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)
        return ans[k-1]