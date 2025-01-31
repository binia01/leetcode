class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        c = s + s
        if goal in c:
            return True
        return False 