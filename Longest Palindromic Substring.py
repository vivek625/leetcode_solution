class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s = 'abb'
        if len(s)<1 or s == s[::-1]:
            return (s)
        check = 1
        st = 0
        end = 0

        for i in range(len(s)):
            l = i
            r = i+1
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    l = l-1
                    r = r+1
                else:
                    break
            my_len = r-1-l
            if my_len > check:
                check = my_len
                st = l+1
                end = r-1

        for i in range(len(s)):    
            l = i
            r = i
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    l = l-1
                    r = r+1
                else:
                    break
            my_len = r-1-l
            if my_len > check:
                check = my_len
                st = l+1
                end = r-1

        return ( s[st:end+1])
