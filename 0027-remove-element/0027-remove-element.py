class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for x in nums:
            if x == val:
                pass
            else:
                nums[k] = x
                k += 1
            print(nums)
        print(k)
        return k
        