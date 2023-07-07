class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums3 = [0] * (m+n)
        j = 0
        k = 0
        for i in range(m+n):
            if j == m:
                nums3[i] = nums2[k]
                k += 1
            elif k == n:
                nums3[i] = nums1[j]
                j += 1
            elif nums1[j] > nums2[k]:
                nums3[i] = nums2[k]
                k += 1
            else:
                nums3[i] = nums1[j]
                j += 1

        for i in range(m+n):
            nums1[i] = nums3[i]
