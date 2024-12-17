'''
给定一个整数数组 nums 和一个整数目标值 target,
请你在该数组中找出 和为目标值 target  的那 两个 整数,并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案
https://leetcode.cn/problems/two-sum/
'''

nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        print(len(nums)-2)
        for i in range(len(nums)-2+1):
            print(i)
            j=i
            for n in range(i,len(nums)-1):
                print(nums[i]," ",nums[j+1])
                if nums[i]+nums[j+1]==target:
                    result.append(i)
                    result.append(j+1)
                    break
                else:
                    j+=1


        return result
        # pass

# Solution()
a=Solution().twoSum(nums,target)
print(a)
# print(result)