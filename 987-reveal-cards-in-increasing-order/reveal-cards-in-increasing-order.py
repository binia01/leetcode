class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        res= [0] * n
        queue = deque()
        for i in range(n):
            queue.append(i)

        for c in deck:
            res[queue.popleft()] = c

            if queue:
                queue.append(queue.popleft())
        return res

        