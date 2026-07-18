import heapq

class Solution:
    def minimumEffortPath(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        # Distance matrix to store minimum effort
        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0

        # Min heap: (effort, row, col)
        heap = [(0, 0, 0)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            curr_effort, r, c = heapq.heappop(heap)

            if r == rows - 1 and c == cols - 1:
                return curr_effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(
                        curr_effort,
                        abs(heights[r][c] - heights[nr][nc])
                    )

                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))

        return 0