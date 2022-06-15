class py_solution:
   def validcheck(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

ch = py_solution()
print(ch.validcheck("{"))
print(ch.validcheck("{}"))
print(ch.validcheck("{]"))
print(ch.validcheck("{)"))
print(ch.validcheck("{}{}[](){}"))
print(ch.validcheck("{}}}{{{}"))
print(ch.validcheck("{())(}"))
print(ch.validcheck("{}[][]{}()"))
