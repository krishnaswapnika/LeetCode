class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles
        while empty >= numExchange:
            new_full = empty//numExchange
            drunk += new_full
            empty = empty % numExchange + new_full
        return drunk
