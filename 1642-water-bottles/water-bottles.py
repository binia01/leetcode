class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        temp = numBottles
        while temp >= numExchange:
            rem =  temp%numExchange
            temp //= numExchange
             
            ans += temp
            temp += rem 
            
        return ans

      
        