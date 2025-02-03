class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_count = {}
        lose_count = {}
        ans = [[],[]]
        for i in range(len(matches)):
            if matches[i][0] in win_count:
                win_count[matches[i][0]] +=1
            else:
                win_count[matches[i][0]] = 1
        for i in range(len(matches)):
            if matches[i][1] in lose_count:
                lose_count[matches[i][1]] += 1
            else:
                lose_count[matches[i][1]] = 1
        for key in win_count:
            if key not in lose_count:
                ans[0].append(key)
        for key in lose_count:
            if lose_count[key] == 1:
                ans[1].append(key)
        for num in ans:
            num.sort()
        return ans



        