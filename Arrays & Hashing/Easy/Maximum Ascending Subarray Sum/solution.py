class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        currentSum = nums[0]
        maxSum = nums[0]

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                currentSum += nums[i]

            else:
                currentSum = nums[i]

            maxSum = max(maxSum, currentSum)

        return maxSum