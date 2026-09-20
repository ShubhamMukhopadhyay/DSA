class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        seen = {}

        for i in range(n):
            if nums[i] in seen:
                if i - seen[nums[i]] <=k :
                    return True

            seen[nums[i]] = i
        return False