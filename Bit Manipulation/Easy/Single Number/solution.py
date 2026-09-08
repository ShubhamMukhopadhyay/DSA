class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            count = 0

            for x in nums:
                if x == num:
                    count += 1

            if count == 1:
                return num