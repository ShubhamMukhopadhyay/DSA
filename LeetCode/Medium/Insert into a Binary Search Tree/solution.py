# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        newNode = TreeNode(target)

        if root == None:
            return newNode

        curr = root

        while curr != None:
            if target < curr.val:
                if curr.left != None:
                    curr = curr.left

                else:
                    curr.left = newNode
                    break

            else:
                if curr.right != None:
                    curr = curr.right

                else:
                    curr.right = newNode
                    break

        return root