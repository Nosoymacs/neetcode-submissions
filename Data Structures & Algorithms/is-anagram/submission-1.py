class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        frequencies = {}

        for letter in s:
            frequencies[letter] = frequencies.get(letter, 0) + 1

        for letter in t:
            if frequencies.get(letter, 0) == 0:
                return False

            frequencies[letter] -= 1

        return True

        
        


        