class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # for i in range(len(heights)):
        #     for j in range(len(heights)-i-1):
        #         if heights[j] < heights[j+1]:
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        #             names[j], names[j+1] = names[j+1], names[j]
        # return names

        # for i in range(len(heights)):
        #     min_num = i
        #     for j in range(i+1, len(heights)):
        #         if heights[min_num] <  heights[j]:
        #             min_num = j
        #     heights[i], heights[min_num] = heights[min_num], heights[i]
        #     names[i], names[min_num] = names[min_num], names[i]

        # return names

        for i in range(1, len(heights)):
            key = heights[i]
            key_name = names[i]
            j = i-1
            while j >=0 and key > heights[j]:
                heights[j+1] = heights[j]
                names[j+1] = names[j]
                j -= 1
            heights[j+1] = key
            names[j+1] = key_name
        return names


