class ProductOfNumbers:

    def __init__(self):
        self.stk = [1]
        

    def add(self, num: int) -> None:
        if num != 0:
            self.stk.append(self.stk[-1] * num)
        else:
            self.stk = [1]

    def getProduct(self, k: int) -> int:
        if len(self.stk) <= k:
            return 0
        else:
            return self.stk[-1]//self.stk[len(self.stk)-1-k]

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)