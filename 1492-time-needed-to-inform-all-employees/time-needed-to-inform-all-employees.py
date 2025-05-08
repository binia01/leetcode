class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(num):
            max_time = 0
            for sub in graph[num]:
                max_time = max(max_time, dfs(sub) + informTime[num])
            return max_time

        graph = defaultdict(list)
        for i, mng_id in enumerate(manager):
            if mng_id != -1:
                graph[mng_id].append(i)

        return dfs(headID)    
        