class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        if nums[0] == 0 and n > 1:
            return False
        for i in range(1, n-1):
            if nums[i] == 0:
                j = 1
                while (i-j) > -1:
                    if nums[i-j] > j:
                        break
                    j += 1
                if (i - j) == -1:
                    return False
        return True