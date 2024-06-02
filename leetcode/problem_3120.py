### Problem 3120. Number of Special Characters in a String (Easy): https://leetcode.com/problems/number-of-special-characters-in-a-string/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special = {}
        unique = ''
        for letter in word:
            isupper = letter.isupper()
            if(letter not in special):
                special[letter] = 1
                if(isupper):
                    if(letter.lower() not in special):
                        unique += letter
                else:
                    if(letter.upper() not in special):
                        unique += letter
            else:
                special[letter] += 1
        count = 0
        for letter in unique:
            if(letter.isupper() and (letter.lower() in special)):
                count += 1
            elif(letter.islower() and (letter.upper() in special)):
                count += 1
        return count