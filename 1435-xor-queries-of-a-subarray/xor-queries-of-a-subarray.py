class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        res = [0] * (len(arr) + 1)

        for idx, num in enumerate(arr):
            res[idx + 1] = res[idx] ^ num

        for left, right in queries:
            ans.append(res[left] ^ res[right + 1])

        return ans