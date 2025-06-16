class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node_index):
            if node_colors[node_index]:
                return node_colors[node_index] == 2
            node_colors[node_index] = 1
            for next_node_index in graph[node_index]:
                if not dfs(next_node_index):
                    return False
            node_colors[node_index] = 2
            return True

        total_nodes = len(graph)
        node_colors = [0] * total_nodes
        safe_nodes = [node_index for node_index in range(total_nodes) if dfs(node_index)]
        return safe_nodes
        