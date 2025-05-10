class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def func(vert):
            if parent[vert] != vert:
                parent[vert] = func(parent[vert])
            return parent[vert]

        parent = list(range(len(edges) + 1))

        for a,b in edges:
            lead_a = func(a)
            lead_b = func(b)

            if lead_a == lead_b:
                return [a, b]

            parent[lead_a] = lead_b
        
        return []
        