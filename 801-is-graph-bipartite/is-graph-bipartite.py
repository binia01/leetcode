class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        res = [0] * len(graph)

        def traverse(node):
            if res[node] == 0: 
                res[node] = 1

            q = deque([node])
            while q:
                curr = q.popleft()
                color = res[curr]
                for neb in graph[curr]:
                    if res[neb] and color == res[neb]: 
                        return False
                        
                    if not res[neb]:
                        q.append(neb)
                        res[neb] = -1 if color == 1 else 1

            return True
                
        for i in range(len(graph)):
            if res[i] == 0:  
                if not traverse(i):
                    return False

        return True