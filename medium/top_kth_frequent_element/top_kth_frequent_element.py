class Solution:
    def topKFrequent(nums, k):
        # create hashmap as key value pair, where key as an inter in list, 
        # value as amount of int appears in the list
        # then sort out the dict as it's value to decending order, 
        # return kth most frequent key.
        num_dict = {}
        for num in nums:
            num_dict[num] = 1 + num_dict.get(num, 0)
        # this is same thing as 
        # for num in nums:
        #     if num in num_dict:
        #         num_dict[num] += 1
        #     else:
        #         num_dict[num] = 1
        sorted_dict = dict(sorted(num_dict.items(), key=lambda item: item[1], reverse = True))
        return list(sorted_dict)[:k]
            

        
