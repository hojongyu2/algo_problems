# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

def is_valid_anagram(s,t):
    if len(s) != len(t):
        return False
    
    string1_counter, string2_counter = {} ,{}
    
    # for letter in s:
    #     if letter in string1_counter:
    #         string1_counter[letter] += 1
    #         string2_counter[letter] += 1
    #     else:
    #         string1_counter[letter] = 1
    #         string2_counter[letter] = 1
    
    for letter in s:
        string1_counter[letter] = 1 + string1_counter.get(letter, 0)
        string2_counter[letter] = 1 + string2_counter.get(letter, 0)
    
    return string1_counter == string2_counter
            
    

string1 = "anagram"
string2 = "arnaamg"

print(is_valid_anagram(string1, string2))