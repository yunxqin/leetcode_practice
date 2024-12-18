'''给定一个字符串 s,请你找出其中不含有重复字符的最长子串的长度。'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        flag=1
        for i in range(0,len(s)):
            j=i
            while len(set(s[i:j+1]))==len(s[i:j+1]) and j<len(s)-1:
                print(s[i:j+1])
                j+=1
            if j-i>flag:
                flag=j-i
        print(flag)
        return flag
    
s="abcabcbb"
a=Solution()
a.lengthOfLongestSubstring(s)