class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        seen = {}

        for i in range(n):
            current = nums[i]
            needed = target - current

            if needed in seen:
                return(seen[needed], i)

            seen[current] = i
