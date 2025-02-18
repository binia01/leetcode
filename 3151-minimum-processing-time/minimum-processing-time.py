class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        min_time = float("-inf")
        i = 0
        for p in processorTime:
            min_time = max(min_time, p + tasks[i])
            i += 4
        return min_time
        
        