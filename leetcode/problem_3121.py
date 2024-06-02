### Problem 3121. Count the Number of Special Characters II (Medium): https://leetcode.com/problems/count-the-number-of-special-characters-ii/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special = {}
        unique = ''
        for i in range(len(word)):
            letter = word[i]
            isupper = letter.isupper()
            if(letter not in special):
                if(isupper):
                    if(letter.lower() not in special):
                        unique += letter
                else:
                    if(letter.upper() not in special):
                        unique += letter
                special[letter] = i
            else:
                if(not isupper):
                    special[letter] = i 

        print(special, unique)
        count = 0
        for letter in unique:
            isUpper = letter.isupper()
            if(isUpper):
                if((letter.lower() in special) and (special[letter.lower()] < special[letter])):
                    count += 1
            else:
                if((letter.upper() in special) and (special[letter.upper()] > special[letter])):
                    count += 1
        return count