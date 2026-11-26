class Solution:
    def canAliceWin(self, n: int) -> bool:
        take = 10

        while n >= take:
            n -= take
            take -= 1

        return take % 2 == 1