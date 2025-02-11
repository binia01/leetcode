class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = list(map(str, nums))

        for i in range(len(n)):
            for j in range(len(n) - 1 - i):
                if int(n[j] + n[j+1]) < int(n[j+1] + n[j]):
                    n[j], n[j+1] = n[j+1], n[j]
        
        return "0" if n[0] == "0" else "".join(n)




