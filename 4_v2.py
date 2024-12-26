'''给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数 。
算法的时间复杂度应该为 O(log (m+n))'''

from typing import List

nums1 = [1,2,4,8,10,15,18,19] 
nums2 = [3,4,9,11,15,16,17]


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素l
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """
            # global m,n
            print(f"k: {k}\n")
            index1, index2 = 0, 0

            # nm, nn = len(nums1), len(nums2)

            while True:
                # 特殊情况
                # print(f"index1: {index1} index2: {index2}")
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1+k // 2 - 1, n - 1)
                newIndex2 = min(index2+k // 2 - 1, m - 1)
                print(f"nums1:{nums1[index1:newIndex1+1]} \nnums2:{nums2[index2:newIndex2+1]}")
                # print(f"newIndex1: {newIndex1} newIndex2: {newIndex2}")
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                print(f"pivot1: {pivot1}  pivot2: {pivot2}")
                if pivot1 <= pivot2:
                    k -= newIndex1-index1+1
                    print(f"k: {k}")
                    index1 = newIndex1 + 1
                    # print(f"index1: {index1}")
                else:
                    k -= newIndex2-index2+1
                    # nums2=nums2[newIndex2:]
                    print(f"k: {k}")
                    index2 = newIndex2 + 1
                    # print(f"index2: {index2}")
                print("\n")
        m, n = len(nums1), len(nums2)
        print(f"m: {m}  n: {n}")
        totalLength = m + n
        print(f"totalLength: {totalLength}\n")
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


a=Solution()
a.findMedianSortedArrays(nums1,nums2)