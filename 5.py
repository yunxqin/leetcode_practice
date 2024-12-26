#longest-palindromic-substring/description/
"给你一个字符串 s,找到 s 中最长的回文子串。"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        elif len(s)==2 and s[1]==s[0]:
            return s
        elif len(s)==2 and (s[0]!=s[1]):
            return s[0]
        else:
            ##bcddcb || abcba
            #1.abcba
            flag=1
            r_length1=1
            r_s1=0
            for i in range(1,len(s)-1):
                start1=i
                start2=i
                while start1+1<len(s) and start2>=0 and s[start1+1]==s[start2-1]:
                    flag+=2
                    start1+=1
                    start2-=1
                if flag>r_length1:
                    r_length1=flag
                    r_s1=i
                    flag=1
                flag=1

            half_length1=int((r_length1-1)/2)

            if r_length1>1:
                res1_=s[(r_s1-half_length1):(r_s1+half_length1+1)]
            else:
                res1_=s[0]
            #2.bcddcb
            flag=1
            r_length2=0
            r_s2=0
            for i in range(0,len(s)-1):
                start=i
                if s[start]==s[start+1] and start+1<len(s):
                    flag=2
                    start1=start-1
                    start2=start+1+1
                    # print(start2)
                    r_s2=i
                    while start2<len(s) and s[start1]==s[start2] and start1>=0:
                        flag+=2
                        start1-=1
                        start2+=1
                    if flag>r_length2:
                        r_length2=flag
                        r_s2=i
            half_length2=int(r_length2/2)
            print(f"flag: {flag}")
            if flag>1:
                res2_=s[r_s2-half_length2+1:r_s2+half_length2+1]
            else:
                res2_=s[0]
            if len(res2_)<len(res1_):
                return res1_
            else:
                return res2_


a="abcdefghijbji"

b=Solution()
c=b.longestPalindrome(a)
print(c)