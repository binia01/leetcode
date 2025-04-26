class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [defaultdict(list) for _ in range(2)]

        for u, v in redEdges:
            res[0][u].append(v)
        for u, v in blueEdges:
            res[1][u].append(v)
        
        ans = [-1] * n
        seen = set()
        q = deque([(0,0), (0,1)])
        dist = 0
        while q:
            for _ in range(len(q)):
                node, color = q.popleft()
                if ans[node] == -1:
                    ans[node] = dist
                
                seen.add((node, color))
                color ^= 1
                for neighbor in res[color][node]:
                    if (neighbor, color) not in seen:
                        q.append((neighbor, color))
            dist+=1
        return ans
            


        