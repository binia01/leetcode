class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    graph[i+1].append(j+1)

        seen = set()
        def dfs(node):
            nonlocal ans
            seen.add(node)
            for n in graph[node]:
                if n not in seen:
                    dfs(n)
        
        ans = 0
        for k in range(1, len(isConnected) + 1):
            if k not in seen:
                dfs(k)
                ans += 1
        
        return ans