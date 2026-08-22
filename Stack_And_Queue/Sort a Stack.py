class Solution:
    def sortStack(self, st):
        ext = []
        while st:
            x = st.pop()
            while ext and ext[-1] < x:
                st.append(ext.pop())
            ext.append(x)
        while ext:
            st.append(ext.pop())
