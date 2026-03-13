# 1. 冒泡排序
def bubble_sort(arr):
    nums = arr[:]
    n = len(nums)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# 测试
print("冒泡排序：", bubble_sort([5, 2, 9, 1, 3]))