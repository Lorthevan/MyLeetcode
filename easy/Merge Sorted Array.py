class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
            初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
            你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
        """
        # 偷鸡玩法
        # for i in range(n):
        #     nums1[m] = nums2[i]
        #     m += 1
        # nums1.sort()
        for i in range(n):
            for j in range(m):
                if nums2[i] <= nums1[j]:
                    for k in range(m, j, -1):
                        nums1[k] = nums1[k-1]
                    nums1[j] = nums2[i]
                    m += 1
                    break
            else:
                nums1[m] = nums2[i]
                m += 1


nums1 = [1,2,3,0,0,0]
c = Solution()
c.merge(nums1, 3, [2,5,6], 3)
print(nums1)