class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        for i in range(len(command)):
            if command[i] == "G":
                ans += command[i]
            elif command[i] == "(":
                if command[i+1] == ")":
                    ans += "o"
                else:
                    ans += "al"
        return ans



        