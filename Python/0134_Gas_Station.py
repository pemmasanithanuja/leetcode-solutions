class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        current_gas = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            total_gas += diff
            current_gas += diff

            # If current gas becomes negative, restart from next station
            if current_gas < 0:
                start = i + 1
                current_gas = 0

        # If total gas is negative, completing the circuit is impossible
        if total_gas < 0:
            return -1

        return start