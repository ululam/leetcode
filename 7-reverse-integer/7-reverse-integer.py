BOUND = 2 << 31 - 1

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        sign = -1 if x < 0 else 1

        y = 0
        reminder = sign * x
        while reminder > 0:
            digit = reminder % 10
            reminder = int(reminder / 10)
            y = y * 10 + digit

        if y > BOUND:
            return 0
            
        return sign * y