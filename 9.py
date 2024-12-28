'''给你一个整数x,如果x是一个回文整数,返回true;否则,返回false。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如,121是回文,而123不是。'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x_=x
        input_list=[]
        r_input_list=[]
        while x_!=0:
            input_list.append(int(x_%10))
            r_input_list.insert(0,int(x_%10))
            x_=int(x_/10)
        for i in range(len(input_list)):
            if input_list[i]==r_input_list[i]:
                continue
            else:
                return False
        return True
    
        # #分长度是单数还是双数
        # if len(x)%2=0:
        #     pass
        # else:
        #     pass


a=Solution()
b=11234543211
c=a.isPalindrome(b)
print(c)
