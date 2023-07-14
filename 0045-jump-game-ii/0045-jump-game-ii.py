class Solution(object):
    def jump(self, nums):
        n = len(nums)
        jump = 1
        i = 0
        if n == 1:
            return 0
        while nums[i] < n-1 - i: #nums[i]위치에서 nums[n-1]에 도달할 수 없는 동안
            print('i= ',i)
            jump += 1
            #nums[i]에서 점프해서 갈 수 있는 위치 중, nums[n-1]과 가장 가까워질 수 있는 값을 찾는다.
            dis = []
            for j in range(i+1,i+nums[i]+1):
                dis.append((n-1)-(j+nums[j]))
            i += dis.index(min(dis)) + 1
        return jump