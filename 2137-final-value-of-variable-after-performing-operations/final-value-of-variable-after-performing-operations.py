class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        add = ["++X", "X++"]
        sub = ["--X",'X--']
        count = 0
        for op in operations:
            if op in add:
                count+=1
            else:
                count-=1
        return count
        