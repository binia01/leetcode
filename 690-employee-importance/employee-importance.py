"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = defaultdict(list)

        for _, val in enumerate(employees):
            res[val.id] = val.subordinates
        ans = 0
        seen = set()
        seen.add(id)
        stack = [id]
        while stack:
            node = stack.pop()
            for _ , val in enumerate(employees):
                if val.id == node:
                    ans += val.importance
            for new_node in res[node]:
                if new_node not in seen:
                    seen.add(new_node)
                    stack.append(new_node)
            
        return ans
        