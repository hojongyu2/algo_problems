class Solution:
    def isPalindrome(self, s: str) -> bool:
        # change it to all lowercase
        # either loop or regex to get rid of non-alphanumeric, 
        # then use reverse and set it as a new string
        # then return reverse == non-reverse

        filtered = "".join(filter(str.isalnum, s)).lower()
        return filtered == filtered[::-1]