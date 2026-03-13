def bubble_sort(arr):
    # 先复制一份列表，避免直接修改原数据
    nums = arr.copy()
    n = len(nums)

    # 外层循环控制排序轮数
    for i in range(n - 1):
        # 用于判断这一轮是否发生交换
        swapped = False

        # 每一轮都会把当前最大的数“冒泡”到后面
        # 所以后面已经排好序的部分可以不用再比较
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                # 如果前一个数比后一个数大，就交换位置
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        # 如果这一轮一次交换都没有发生
        # 说明列表已经有序，可以提前结束
        if not swapped:
            break

    return nums


# 测试
data = [64, 34, 25, 12, 22, 11, 90]
result = bubble_sort(data)

print("原数组：", data)
print("排序后：", result)