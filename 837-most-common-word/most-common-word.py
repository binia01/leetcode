class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = {}
        words = re.findall(r'\w+', paragraph.lower())

        for word in words:
            if word not in banned:
                count[word] =count.get(word,0) + 1
        max_word = ''
        max_count = 0
        for word, counts in count.items():
            if counts > max_count:
                max_word = word
                max_count = counts
        return max_word
        
        