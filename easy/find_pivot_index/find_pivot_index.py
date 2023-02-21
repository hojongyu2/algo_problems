nums = [1,7,3,6,5,6]
def find_pivot_number(nums):
    left_num = 0
    right_num = sum(nums) # find sum of all numbers and assigned it to the string as number
    for i, ele in enumerate(nums): #iterate elements through the loop
        right_num -= ele 
        if left_num == right_num: # if sum of all the numbers strickly to the left is equal to sum of all the numbers to the right
            return i # return index of pivot number
        left_num += ele
    return -1 # if there is no pivor number, then return -1
print(find_pivot_number(nums))
# 28 - 1 - 7 - 3 - 6 = 17
# 0 + 1 + 7 + 3  = 11