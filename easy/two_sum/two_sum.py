def two_sum(number_of_array, target):
    # create number_dict/hash map
    # create iteration using for loop and start to make key : value
    # create difference variable diff = target - number[i]
    # check if the diff is already exist in the dict and if it does, return [index, difference index]
    # if it does not exist, then create one. key : value
    number_dict = {}
    for number in range(len(number_of_array)):
        number_one = number_of_array[number]
        difference = target - number_one
        if difference in number_dict:
            return [number_of_array.index(difference), number]
        else:
            number_dict[number_one] = 1
