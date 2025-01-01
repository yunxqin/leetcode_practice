'''给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s 的，而不是部分字符串。'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i=0
        new_p=""
        flag_point=0
        flag_star=0
        j=0
        while i<len(s) and j<len(p):
            if s[i]==p[j]:
                i+=1
                j+=1
                continue
            elif s[i]!=p[j] and p[j]==".":
                new_p+=s[i]
                i+=1
                j+=1
                flag_point=1
                continue
            elif s[i]!=p[j] and p[j]=="*":
                flag_star=1
                new_p+=s[i]
                j+=1
                print(i)
                while i+1<len(s) and s[i]==s[i+1]:
                    i+=1
                i+=1
                print(f"i:  {i}")
                continue
            else:
                print(f"i: {i}")
                print(f"j: {j}")
                return False  
        print(new_p)
        if flag_point==0 and len(s)!=len(p) and flag_star==0:
            print("？")
            return False
        return True

a=Solution()
s="aa"
p="a*"
s="aa"
p="a"
s="aab"
p="a*a*b"
c=a.isMatch(s,p)
print(c)