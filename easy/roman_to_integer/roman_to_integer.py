class Solution:
    def romanToInt(self, s: str) -> int:
        r_to_i = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        output = 0
        for letter in s:
            output += r_to_i[letter]
        # iv = 4
            2
        # iv= 6
        # ix = 9
            2
        # ix = 11
        # xl = 40
        20   
        # xl = 60
        # xc = 90
        20
        # xc = 110
        if "IV" in s:
            output -= 2
        if "IX" in s:
            output -= 2
        if "XL" in s:
            output -= 20
        if "XC" in s:
            output -= 20
        if "CD" in s:
            output -= 200
        if "CM" in s:
            output -= 200

        return output
Console
