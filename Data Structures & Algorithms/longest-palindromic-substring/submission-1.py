class Solution:
    def check(self, l, r, string):
        for i in range(len(string)):
            l=r=i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if len(s[l:r+1])>longestLen:
                    longest=s[l:r+1]
                    longestLen=len(s[l:r+1])
                l-=1
                r+=1

    def longestPalindrome(self, s: str) -> str:
        longest=""
        longestLen=0
        

        for i in range(len(s)):
            l=r=i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if len(s[l:r+1])>longestLen:
                    longest=s[l:r+1]
                    longestLen=len(s[l:r+1])
                l-=1
                r+=1
        for i in range(len(s)):
            l=i
            r=i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if len(s[l:r+1])>longestLen:
                    longest=s[l:r+1]
                    longestLen=len(s[l:r+1])
                l-=1
                r+=1
        
        return longest
