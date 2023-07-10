class Solution(object):
    def majorityElement(self, nums):
        maj = None
        cnt = 0
        for i in nums:
            if cnt == 0:
                maj = i
            cnt += (1 if i == maj else -1)
        return maj