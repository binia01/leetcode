class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next_num(n):
            output = 0

            while n:
                dig = n % 10
                output += dig ** 2
                n = n // 10
            return output
        slow = get_next_num(n)
        fast = get_next_num(get_next_num(n))
        while slow != fast:
            if fast == 1: 
                return True
            slow = get_next_num(slow)
            fast = get_next_num(get_next_num(fast))
        return slow == 1
        