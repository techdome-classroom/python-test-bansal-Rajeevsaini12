class Solution(object):
    def isValid(self, s):
        stack=[]
        map={ ')':'(' , '}':'{', ']':'['}

        for char in s:
            if char in map:
                top_ele=stack.pop() if stack else "#"
                if map[char] != top_ele:
                    return False
            else:
                stack.append(char)
        return True              

s=Solution()
print(s.isValid("{}"))
print(s.isValid("()"))
print(s.isValid("{)"))

