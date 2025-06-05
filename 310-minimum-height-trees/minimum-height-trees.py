class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
      
        graph = defaultdict(list)
        degree = [0] * n
      
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            degree[node1] += 1
            degree[node2] += 1
      
        leaves_queue = deque(i for i in range(n) if degree[i] == 1)
        min_height_trees = []
    
        while leaves_queue:
            min_height_trees.clear()
            for _ in range(len(leaves_queue)):
                current_node = leaves_queue.popleft()
                min_height_trees.append(current_node)
                for neighbor in graph[current_node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves_queue.append(neighbor)
        return min_height_trees
        