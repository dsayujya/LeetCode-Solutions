class Solution:
    def longestPalindrome(self, s: str) -> str:
        mid = 0
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if mid <(r-l+1):
                    mid = r-l+1
                    right = r
                    left = l
                r+=1
                l-=1    
                    
            l,r = i, i+1
            while l>= 0 and r< len(s) and s[l] == s[r]:
                if mid<(r-l+1):
                    mid = r-l+1
                    right = r
                    left = l

                l-=1
                r += 1
        return s[left:right+1]