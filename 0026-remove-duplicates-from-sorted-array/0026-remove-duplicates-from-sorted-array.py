class Solution(object):
    def removeDuplicates(self, nums):
        k = 1
        e = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != e:
                nums[k] = nums[i]
                e = nums[i]
                k += 1
        return k
