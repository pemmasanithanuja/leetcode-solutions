class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()

        left = 0
        right = len(people) - 1
        boats = 0

        while left <= right:
            # Try to put the lightest person with the heaviest person
            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            boats += 1

        return boats