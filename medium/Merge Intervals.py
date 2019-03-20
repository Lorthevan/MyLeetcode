# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda i: i.start)
        
        flag = 0
        while flag != len(intervals):
            flag = len(intervals)
            for i in range(len(intervals) - 1, 0, -1):
                if intervals[i - 1].end >= intervals[i].end:
                    intervals.pop(i)
                elif intervals[i - 1].end >= intervals[i].start:
                    intervals[i - 1].end = intervals[i].end
                    intervals.pop(i)
        
        return intervals


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out