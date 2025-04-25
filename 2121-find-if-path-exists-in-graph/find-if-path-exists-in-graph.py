class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        res = defaultdict(list)
        for u, v in edges:
            res[u].append(v)
            res[v].append(u)
        seen = set()
        seen.add(source)
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for new_node in res[node]:
                if new_node not in seen:
                    seen.add(new_node)
                    stack.append(new_node)
        return False
        