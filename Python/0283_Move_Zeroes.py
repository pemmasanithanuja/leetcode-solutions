class Solution:
    def moveZeroes(self, nums):
        insert_pos = 0

        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Fill remaining positions with zeros
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1