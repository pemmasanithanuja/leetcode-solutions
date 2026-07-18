class Solution:
    def partitionLabels(self, s):
        # Store the last index of each character
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        result = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            # Extend the current partition boundary
            end = max(end, last[ch])

            # If we reach the boundary, make a partition
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result