class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        summed_value = 0   
        for letter in range(len(s)):
            if letter + 1 < len(s) and roman[s[letter]] < roman[s[letter + 1]]:
                summed_value -= roman[s[letter]]
            else:
                summed_value += roman[s[letter]]
        return summed_value