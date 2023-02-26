class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # You must write an algorithm with O(log n) runtime complexity.
        # middleindex = array[middle] if this value is target number, then return index
        # else if value < target, then narrow down our search array towards the left side only
        # same logic for the value > target
        # do this until you find the target value and if no value then return -1
        first_idx = 0
        last_idx = len(nums)-1 # 5
    
        while first_idx <= last_idx:
            middle_idx = (first_idx + last_idx)//2 # 1 2
            if nums[middle_idx] == target:
                return middle_idx
            elif nums[middle_idx] < target:
                first_idx = middle_idx + 1
            else:
                last_idx = middle_idx -1
        return -1