class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for key in rooms[node]:
                dfs(key)
        seen = set()
        dfs(0)
        return len(seen) == len(rooms)