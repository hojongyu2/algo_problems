def contain_duplicate(nums):
    # create dictionary that will store number as a key and number of appearance as a value
    # return True if the value already exist in the dictionary, else return False
    number_dict = {}
    for number in nums:
        if number in number_dict:
            return True
        else:
            number_dict[number] = 1
    return False
