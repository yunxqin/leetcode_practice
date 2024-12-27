class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        z_s_row=numRows
        z_s_line=int(len(s)//(2*numRows-2)+1)*int(1+numRows-2)
        print(z_s_line)
        z_s = [[0 for _ in range(z_s_line)] for _ in range(numRows)]
        print(len(z_s))
        print(len(z_s[0]))
        if numRows==1:
            return s
        else:
            flag=0
            cal_r=0
            set_output=[]
            #一列一列的摆放好
            row_=0
            line_=0
            #以2*numRows-2为一组，分割输入，
            i=0
            while i < len(s):
                print(f"flag: {flag} line: {line_} i: {i}")
                if flag<numRows:
                    z_s[flag][line_]=s[i]
                    flag+=1
                    i+=1
                else:
                    line_+=1
                    flag=numRows-2
                    while flag>=1:
                        z_s[flag][line_]=s[i]
                        flag-=1
                        line_+=1
                        i+=1
                    flag=0
            for _ in range(len(z_s)):
                print(z_s[_])

        #输出结果
        result=""
        for row in range(len(z_s)):
            for line in range(len(z_s[0])):
                if z_s[row][line]!=0:
                    result+=z_s[row][line]
        print(result)
        return result
s="PAYPALISHIRING"
s="A"
print(len(s))
numRows=1
a=Solution()
a.convert(s,numRows)
            # for i in range(0,len(s)):
                
            #     while row_<numRows:
            #         z_s[row_][0]=s[i]
            #         pass
                
            #     pass