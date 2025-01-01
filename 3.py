'''给定一个字符串 s,请你找出其中不含有重复字符的最长子串的长度。'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        if length==0:
            return 0
        elif length==1:
            return 1
        flag=1
        length_=0
        for i in range(0,len(s)):
            j=i
            while len(set(s[i:j+2]))==len(s[i:j+2]) and j<len(s)-1:
                # print(f"flag:{flag}")
                print(s[i:j+1])
                flag+=1
                j+=1
                print(f"flag:{flag}")
            if flag>length_:
                length_=flag
                print(f"length_: {length_}")
                flag=1
            else:
                flag=1
        print(length_)
        return length_
    
s="abcdeb"
a=Solution()
a.lengthOfLongestSubstring(s)