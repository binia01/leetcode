class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(vertex):
            visited[vertex] = True
            vertex_count, edge_count = 1, len(graph[vertex])  
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    additional_vertices, additional_edges = dfs(neighbor)
                    vertex_count += additional_vertices
                    edge_count += additional_edges
            return vertex_count, edge_count

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
          
        visited = [False] * n  
        complete_components_count = 0  
      
        for i in range(n):
            if not visited[i]:
                vertex_count, edge_count = dfs(i)
                if vertex_count * (vertex_count - 1) == edge_count:
                    complete_components_count += 1
                  
        return complete_components_count
        