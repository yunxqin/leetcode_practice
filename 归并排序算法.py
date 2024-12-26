def merge_sort(arr):
    # 递归终止条件：如果数组只有一个元素或为空，直接返回
    if len(arr) <= 1:
        return arr

    # 1. 分割数组
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. 递归地对左右两部分进行归并排序
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 3. 合并左右部分
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """合并两个有序数组"""
    merged = []
    i = j = 0

    # 依次比较两个数组中的元素，将较小的元素加入合并结果
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # 如果左数组还有剩余，直接加入合并结果
    while i < len(left):
        merged.append(left[i])
        i += 1

    # 如果右数组还有剩余，直接加入合并结果
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

# 测试
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("归并排序结果：", sorted_arr)
