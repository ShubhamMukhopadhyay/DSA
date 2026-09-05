# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if nums == []:
            return None

        mid_index = len(nums) // 2
        middle_element = nums[mid_index]
        
        root = TreeNode(middle_element)

        left_half = nums[0:mid_index]
        right_half = nums[mid_index + 1 : len(nums)]

        root.left = self.sortedArrayToBST(left_half)
        root.right = self.sortedArrayToBST(right_half)

        return root