class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        mid = (n + 1) // 2

        arr = nums[:]

        small = mid - 1
        large = n - 1

        for i in range(n):
            if i % 2 == 0:
                nums[i] = arr[small]
                small -= 1

            else:
                nums[i] = arr[large]
                large -= 1
