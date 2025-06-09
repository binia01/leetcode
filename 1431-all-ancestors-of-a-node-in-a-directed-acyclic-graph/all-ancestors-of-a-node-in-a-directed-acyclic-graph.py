class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def bfs(start_node):
            queue = deque([start_node]) 
            visited = {start_node}  
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        ancestors[neighbor].append(start_node)

        graph = defaultdict(list)
        for parent, child in edges:
            graph[parent].append(child)
      
        ancestors = [[] for _ in range(n)]
        for node in range(n):
            bfs(node)
        return ancestors

        