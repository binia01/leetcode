class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dictionary = {}
        row = ["qwertyuiop","asdfghjkl", "zxcvbnm"]
        for i in range(3):
            for j in range(len(row[i])):
                dictionary[row[i][j]] = i
        
        ans = []
        for i in range(len(words)):
            flag = True
            row =  dictionary[words[i][0].lower()]
            for j in words[i]:
                if dictionary[j.lower()] != row:
                    flag = False
                    break
            if flag:
                ans.append(words[i])
        return ans
                


        