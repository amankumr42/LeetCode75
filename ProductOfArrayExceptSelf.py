def productExceptSelf(nums):
    if len(nums) == 0:
        return []

    result = [1 for num in nums]
    leftProduct = [1 for num in nums]
    rightProduct = [1 for num in nums]

    for leftIndex in range(len(nums)-1):
        rightIndex = len(nums) - leftIndex - 1 

        leftNum = nums[leftIndex]
        rightNum = nums[rightIndex]

        leftProduct[leftIndex+1] = leftProduct[leftIndex] * leftNum
        rightProduct[rightIndex-1] = rightProduct[rightIndex] * rightNum

    for index in range(len(nums)):
        result[index] = leftProduct[index] * rightProduct[index]

    return result