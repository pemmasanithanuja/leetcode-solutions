class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Sort by ending time
        intervals.sort(key=lambda x: x[1])

        count = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            # Overlapping interval found
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]

        return count