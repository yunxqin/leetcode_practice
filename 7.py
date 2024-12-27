'''给你一个32位的有符号整数x ，返回将x中的数字部分反转后的结果。
如果反转后整数超过32位的有符号整数的范围[−231, 231 − 1],就返回0.'''
class Solution:
    def reverse(self, x: int) -> int:
        #判断溢出，反转
        INT_MAX=2**31-1
        INT_MIN=-2**31
        print(INT_MAX)
        INT_MIN_list=[]
        INT_MAX_list=[]

        while INT_MAX !=0:
            INT_MAX_list.insert(0,INT_MAX%10)
            INT_MAX=int(INT_MAX/10)
        print(INT_MAX)
        INT_MIN_list=INT_MAX_list
        INT_MIN_list[-1]=INT_MIN_list[-1]-1

        print(f"INT_MIN_list:{INT_MIN_list}\nINT_MAX_list:{INT_MAX_list}")
        # INT_MIN_=-INT_MIN
        # while INT_MIN !=0:
        #     INT_MIN_list.append(INT_MAX%10)
        #     INT_MAX=int(INT_MAX/10)
        # print(INT_MAX)

        x_list=[]
        x_=x
        fuhao=0
        print(1%10)
        print(-1%10)
        if x==0:
            return 0
        elif x>0:
            while x_ !=0:
                x_list.append(x_%10)
                x_=int(x_/10)
                print(x_)
            print(x_list)
        elif x<0:
            fuhao=1
            x_=-x
            while x_ !=0:
                x_list.append(x_%10)
                x_=int(x_/10)
                print(x_)
            print(x_list)            


            pass
        x_result=0
        print(f"x_list: {x_list} \nfuhao: {fuhao}")
        #根据x_list计算 溢出与最终答案
        def calculate_result(x_list):
            x_result=0
            for i in range(len(x_list)):
                x_result+=10**(len(x_list)-i-1)*x_list[i]           
            return x_result
        if len(x_list)<len(INT_MAX_list):
            for i in range(len(x_list)):
                x_result+=10**(len(x_list)-i-1)*x_list[i]
            if fuhao==0:
                return x_result
            else:
                return -x_result
        else:
            if fuhao==0:
                for i in range(len(INT_MAX_list)):
                    if INT_MAX_list[i]>x_list[i]:
                        return calculate_result(x_list)
                    elif INT_MAX_list[i]==x_list[i]:
                        x_result+=10**(len(x_list))*x_list[i] 
                    else:
                        return 0
                    return x_result
            else:
                ##负数 
                for i in range(len(INT_MIN_list)):
                    if INT_MIN_list[i]>x_list[i]:
                        return -calculate_result(x_list)
                    elif INT_MIN_list[i]==x_list[i]:
                        x_result+=10**(len(x_list))*x_list[i] 
                    else:
                        return 0
                    return -x_result   

a=Solution()

b=2147483641
print(a.reverse(b))