'''请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数。

函数 myAtoi(string s) 的算法如下：

空格：读入字符串并丢弃无用的前导空格（" "）
符号：检查下一个字符（假设还未到字符末尾）为 '-' 还是 '+'。如果两者都不存在，则假定结果为正。
转换：通过跳过前置零来读取该整数，直到遇到非数字字符或到达字符串的结尾。如果没有读取数字，则结果为0。
舍入：如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被舍入为 −231 ，大于 231 − 1 的整数应该被舍入为 231 − 1 。
返回整数作为最终结果。'''

class Solution:
    def myAtoi(self, s: str) -> int:
        #丢弃无用的前导空格
        i=0
        bl_num=0
        while i<len(s):
            if s[i]==" ":
                # s=s[1:]
                i+=1
                bl_num+=1
            elif s[i]!=" ":
                break
        s=s[bl_num:]
        print(s)    
        #判断正负号
        neg_or_pos=0
        if s[0]=="-":
            neg_or_pos=1
            s=s[1:]
            
        # #判断符号
        # i=0
        # neg_or_pos=0
        # while not s[i].isdigit() and i < len(s):
        #     if s[i]=="-":
        #         neg_or_pos=1

        #     i+=1
        # ###得到符号

        #如果下一个不是数字 返回0
        if not s[0].isdigit():
            return 0

        ###如果没有数字 返回0
        i=0
        num_exist=0
        while i < len(s):
            if s[i].isdigit():
                num_exist=1
            i+=1
        if num_exist==0:
            return 0
        #通过跳过前置零来读取该整数，直到遇到非数字字符或到达字符串的结尾
        num_result_list=[]
        flag=0
        i=0
        while i < len(s):
            print(i)
            if s[i].isdigit():
                num_result_list.append(int(s[i]))
                flag=1
                i+=1
            elif not s[i].isdigit() and flag==0:
                i+=1
                continue
            elif not s[i].isdigit() and flag==1:
                break
        print(f"num_result_list: {num_result_list}")
        #得到最终的数字字符串num_result_list  （正序）["1","2","3"]->123
        #判断是否溢出
        INT_MAX=2**31-1
        INT_MIN=-2**31
        INT_MIN_list=[]
        INT_MAX_list=[]
        while INT_MAX !=0:
            INT_MAX_list.insert(0,INT_MAX%10)
            INT_MAX=int(INT_MAX/10)

        INT_MIN_list=INT_MAX_list
        INT_MIN_list[-1]=INT_MIN_list[-1]-1
        x_result=0
        def calculate_result(x_list):
            x_result=0
            for i in range(len(x_list)):
                x_result+=10**(len(x_list)-i-1)*x_list[i]           
            return x_result
        if len(num_result_list)<len(INT_MAX_list):
            for i in range(len(num_result_list)):
                x_result+=10**(len(num_result_list)-i-1)*num_result_list[i]
            if neg_or_pos==0:
                return x_result
            else:
                return -x_result
        else:
            if neg_or_pos==0:
                for i in range(len(INT_MAX_list)):
                    if INT_MAX_list[i]>num_result_list[i]:
                        return calculate_result(num_result_list)
                    elif INT_MAX_list[i]==num_result_list[i]:
                        x_result+=10**(len(num_result_list))*num_result_list[i] 
                    else:
                        return 0
                    return x_result
            else:
                ##负数 
                for i in range(len(INT_MIN_list)):
                    if INT_MIN_list[i]>num_result_list[i]:
                        return -calculate_result(num_result_list)
                    elif INT_MIN_list[i]==num_result_list[i]:
                        x_result+=10**(len(num_result_list))*num_result_list[i] 
                    else:
                        return 0
                    return -x_result        

a=Solution()
b="words and 987" 
b="   -042" 
c=a.myAtoi(b)
print(c)





