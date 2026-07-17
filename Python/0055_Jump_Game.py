class Solution:
    def canJump(self, nums):
        max_reach = 0

        for i in range(len(nums)):
            # If current index is not reachable
            if i > max_reach:
                return False

            # Update the farthest reachable position
            max_reach = max(max_reach, i + nums[i])

        return True  