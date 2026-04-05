class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token in "+-*/":
                secondOperand = stk.pop()
                firstOperand = stk.pop() 
                res = 0
                if token == "+":
                    res = firstOperand + secondOperand
                elif token == "-":
                    res = firstOperand - secondOperand
                elif token == "*":
                    res = firstOperand * secondOperand
                else:
                    res = int(firstOperand / secondOperand)
                stk.append(res)                
            else:
                  stk.append(int(token))
     

        return int(stk[0])           