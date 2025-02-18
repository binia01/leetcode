class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n)
        for s, e, v in bookings:
            ans[s-1] += v
            if e < n:
                ans[e] -= v
        ans2 = list(accumulate(ans))
        return ans2        