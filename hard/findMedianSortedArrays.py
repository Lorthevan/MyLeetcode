class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lst = sorted(nums1 + nums2)
        mid, re = divmod(len(lst), 2)
        return (lst[mid]+lst[mid+re-1]) / 2
    