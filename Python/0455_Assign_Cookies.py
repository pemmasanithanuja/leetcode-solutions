class Solution:
    def findContentChildren(self, g, s):
        g.sort()  # Sort children's greed factors
        s.sort()  # Sort cookie sizes

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1  # Child is satisfied
            
            cookie += 1  # Move to next cookie

        return child