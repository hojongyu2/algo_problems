def productExceptSelf(nums):
    output = []
    left = 1
    for num in nums:
        output.append(left)
        left *= num
    right = 1
    for num in range(len(output)-1, -1, -1):
        output[num] *= right
        right *= nums[num]
        
    return output


print(productExceptSelf([1,2,3,4]))