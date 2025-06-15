class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for index, task in enumerate(tasks):
            task.append(index)
      
        tasks.sort()

        answer = []
        priority_queue = []

        num_tasks = len(tasks)
        task_index = 0
        current_time = 0

        while priority_queue or task_index < num_tasks:
            if not priority_queue:
                current_time = max(current_time, tasks[task_index][0])

            while task_index < num_tasks and tasks[task_index][0] <= current_time:
                heapq.heappush(priority_queue, (tasks[task_index][1], tasks[task_index][2]))
                task_index += 1
            processing_time, task_order_index = heapq.heappop(priority_queue)
            answer.append(task_order_index)
            current_time += processing_time
        return answer
