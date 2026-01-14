class Solution:
    def middle(self, a, b, c):
        if a < b < c or c < b < a:
            return b
        elif b < a < c or c < a < b:
            return a
        elif a < c < b or b < c < a:
            return c
