class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        n = len(nums)
        freq = {}

        for num in nums:
            if num not in freq :
                freq[num] = 1

            else:
                freq[num] += 1

        for num in freq:
            if freq[num] > (n / 3):
                result.append(num)

        return result
        
