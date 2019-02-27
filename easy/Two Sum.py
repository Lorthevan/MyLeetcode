class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # solution 1, low
        # s = set(nums)
        # for i in s:
        #     if target-i in s:
        #         if i != target-i:
        #             for x in range(len(nums)):
        #                 if nums[x] == i:break
        #             for y in range(len(nums)):
        #                 if nums[y] == target-i:break
        #             break
        #         elif i == target-i:
        #             for x in range(len(nums)):
        #                 if nums[x] == i:break
        #             for y in range(x+1,len(nums)):
        #                 if nums[y] == i:break
        #             else:
        #                 continue
        #             break
        # if x>y:x,y=y,x
        # return x,y

        # solution 2, muy bien!
        dic = {}
        for index, num in enumerate(nums):
            if target-num in dic:
                return [dic[target-num], index]
            else:
                dic[num] = index


print(Solution().twoSum([3, 2, 4], 6))