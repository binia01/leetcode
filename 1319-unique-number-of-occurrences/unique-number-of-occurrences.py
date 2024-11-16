class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}

        for arrs in arr:
            if arrs in map:
                map[arrs] += 1
            else:
                map[arrs] = 1

        lst = list(map.values())
        lis = list(set(lst))
        if len(lst) == len(lis):
            return True
        return False
        