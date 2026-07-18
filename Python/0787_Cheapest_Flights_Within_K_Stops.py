class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        INF = float('inf')

        prices = [INF] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices[:]   # copy the list

            for u, v, cost in flights:
                if prices[u] != INF:
                    temp[v] = min(temp[v], prices[u] + cost)

            prices = temp

        return -1 if prices[dst] == INF else prices[dst]