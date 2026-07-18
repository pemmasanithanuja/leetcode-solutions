import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)

        visited = [[False] * n for _ in range(n)]

        # Min heap: (time, row, col)
        heap = [(grid[0][0], 0, 0)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            time, r, c = heapq.heappop(heap)

            if visited[r][c]:
                continue

            visited[r][c] = True

            # Reached destination
            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(heap, (new_time, nr, nc))  