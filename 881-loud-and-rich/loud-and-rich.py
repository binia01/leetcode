class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(index):
            if answer[index] != -1:
                return
            answer[index] = index
            for neighbor in graph[index]:
                dfs(neighbor)
                if quiet[answer[neighbor]] < quiet[answer[index]]:
                    answer[index] = answer[neighbor]

        graph = defaultdict(list)
        for richer_person, poorer_person in richer:
            graph[poorer_person].append(richer_person)

        n = len(quiet)
        answer = [-1] * n
     
        for i in range(n):
            dfs(i)

        return answer
        