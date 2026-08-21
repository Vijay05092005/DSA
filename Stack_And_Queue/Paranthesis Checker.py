class Solution:
    def isBalanced(self, s):
        stack=[]
        for x in s:
            if x=='{' or x=='[' or x=='(':
                stack.append(x)
            elif x=='}' or x==']' or x==')':
                if not stack:
                    return False
                y=stack[-1]
                if x=='}' and y!='{':
                    return False
                elif x==']' and y!='[':
                    return False
                elif x==')' and y!='(':
                    return False
                stack.pop()
        return len(stack)==0
class Solution:
    def isBalanced(self, s):
        stack=[]
        check={'}':'{',']':'[',')':'('}
        for x in s:
            if x=='{' or x=='[' or x=='(':
                stack.append(x)
            else: 
                if not stack:
                    return False
                y=stack.pop()
                if y!=check[x]:
                    return False
        return len(stack)==0
