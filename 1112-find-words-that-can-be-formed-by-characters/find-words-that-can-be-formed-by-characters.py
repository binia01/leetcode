class Solution:
    def anagram(self,word, chars):
        count1 = Counter(word)
        count2 = Counter(chars)
        for letter in count1:
            if count1[letter] > count2[letter]:
                return False
        return True
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            if self.anagram(word, chars):
                count += len(word)
        return count
                

        
        
