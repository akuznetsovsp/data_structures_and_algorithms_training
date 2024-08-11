class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        start = newInterval[0]
        end = newInterval[1]

        i = 0
        res = []

        while i < len(intervals) and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1

        while i < len(intervals) and end >= intervals[i][0]:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        res.append([start, end])

        while i < len(intervals) and end < intervals[i][0]:
            res.append(intervals[i])
            i += 1

        return res
