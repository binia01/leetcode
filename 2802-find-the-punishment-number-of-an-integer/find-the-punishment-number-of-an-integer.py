class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_split_to_original(num_str, start_index, target_sum):
            num_length = len(num_str)
            if start_index >= num_length:
                return target_sum == 0
          
            current_num = 0
            for j in range(start_index, num_length):
                current_num = current_num * 10 + int(num_str[j])
                if current_num > target_sum:
                    break
                if can_split_to_original(num_str, j + 1, target_sum - current_num):
                    return True
            return False

        total_sum = 0
        for i in range(1, n + 1):
            square_num = i * i 
            if can_split_to_original(str(square_num), 0, i):
                total_sum += square_num
      
        return total_sum
        