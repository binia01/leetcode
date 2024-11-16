class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}

        for arrs in arr:
            if arrs in map:
                map[arrs] += 1
            else:
                map[arrs] = 1

        return True if (len(set(map.values())) == len(map.values())) else False