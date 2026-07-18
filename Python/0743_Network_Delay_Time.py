import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {}

        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))

        heap = [(0, k)]
        visited = {}

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited[node] = time

            if node in graph:
                for nei, wt in graph[node]:
                    if nei not in visited:
                        heapq.heappush(heap, (time + wt, nei))

        if len(visited) == n:
            return max(visited.values())
        else:
            return -1