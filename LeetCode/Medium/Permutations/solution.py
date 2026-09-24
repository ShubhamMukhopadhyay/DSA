class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools

        perm_iter = permutations(nums)

        # Convert to a list to view or print them
        perm_list = list(perm_iter)
        
        return perm_list