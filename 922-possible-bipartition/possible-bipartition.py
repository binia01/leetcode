class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        res = {}

        for node in range(1, n+1):
            if node not in res:
                queue = deque([node])
                res[node] = 0

                while queue:
                    cur = queue.popleft()
                    for neighbor in graph[cur]:
                        if neighbor in res:
                            if res[neighbor] == res[cur]:
                                return False
                        else:
                            res[neighbor] = 1 - res[cur]
                            queue.append(neighbor)
        
        return True
