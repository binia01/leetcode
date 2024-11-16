class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        alt = [0, gain[0]]

        for i in range (1, n):
            gain[i] = gain[i] + gain[i - 1]
            alt.append(gain[i])


        return max(alt)

        