# 3. 选择排序
def selection_sort(arr):
    nums = arr[:]
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


# 测试
print("选择排序：", selection_sort([5, 2, 9, 1, 3]))