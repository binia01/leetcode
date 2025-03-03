class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count = 0 
        for i in range(len(piles)//3):
            count += piles[len(piles)-((i+1)*2)]
        return count

        