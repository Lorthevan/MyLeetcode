class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        nums.sort()
        length = len(nums)
        res = list()

        for l in range(length - 2):
            if nums[l] > 0:
                break
            if l > 0 and nums[l] == nums[l-1]:
                continue

            m, r = l + 1, length - 1
            while m < r:
                total = nums[l] + nums[m] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    m += 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    while m < r and nums[m] == nums[m+1]:
                        m += 1
                    while m < r and nums[r] == nums[r-1]:
                        r -= 1
                    m += 1
                    r -= 1
        return res