class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = 1
        pos = 1
        for i in range(time):
            pos += direction
            if pos == n:
                direction = -1
            elif pos == 1:
                direction = 1
        return pos

        