class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        st = ""
        
        while columnNumber > 0:
            columnNumber -= 1
            st += chr((columnNumber%26) + ord("A"))
            columnNumber//=26

        return st[::-1]
        