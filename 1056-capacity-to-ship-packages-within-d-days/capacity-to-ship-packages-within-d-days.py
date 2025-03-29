class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def func(capacity):
            cur, count = 0, 1

            for weight in weights:
                cur += weight
                if cur > capacity:
                    count += 1
                    cur = weight
            return count <= days

        left, right = max(weights), sum(weights)

        return left + bisect_left(range(left, right), True, key=func)
        