class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = list()
        for c in s:
            lst.append(c)
            if len(set(lst)) < len(lst):
                lst.pop(0)
        return len(lst)



        # lst = list()
        # st = set()
        #
        # for c in s:
        #     lst.append(c)
        #     st.add(c)
        #
        #     if len(st) < len(lst):
        #         item = lst.pop(0)
        #         if item not in lst:
        #             st.remove(item)
        # return len(lst)