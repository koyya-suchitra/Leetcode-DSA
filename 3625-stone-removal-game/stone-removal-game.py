class Solution:
    def canAliceWin(self, n: int) -> bool:
        for i in range(10, -1,-1):
            if n < i:
                return i%2 != 0
            n -= i
        return False