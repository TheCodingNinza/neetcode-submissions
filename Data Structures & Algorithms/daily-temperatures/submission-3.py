class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        stk.append(Item(temperatures[0], 0))
        ans = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            currTemp = temperatures[i]
            while stk:
                if stk[-1].val < currTemp:
                    temp = stk.pop();
                    ans[temp.index] = i - temp.index
                else:
                    break    
            stk.append(Item(currTemp, i))
        return ans              






class Item:
    def __init__(self, val, index):
        self.val = val
        self.index = index

    def __repr__(self):
        return f"Item(val={self.val}, index={self.index})"           