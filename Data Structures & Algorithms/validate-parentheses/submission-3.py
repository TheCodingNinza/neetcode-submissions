class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stk.append(ch)
            elif ch == ")":
                if not stk:
                    return False
                elif stk[-1] == "(":
                    stk.pop()
                else:
                    return False
            elif ch == "}":
                if not stk:
                    return False
                elif stk[-1] == "{":
                    stk.pop()
                else:
                    return False
            else:
                if not stk:
                    return False
                elif stk[-1] == "[":
                    stk.pop()
                else:
                    return False
        if not stk:
            return True
        else:
            return False                                        