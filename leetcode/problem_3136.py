### Problem 3136. Valid Word (Easy): https://leetcode.com/problems/valid-word/
class Solution:
    def isValid(self, word: str) -> bool:
        result = True
        hasVowel = False
        hasCon = False
        if(len(word) < 3):
            return False
        for letter in word:
            ascii = ord(letter)
            if(not ((ascii >= 97 and ascii < 123) or (ascii >= 65 and ascii < 91) or (ascii >= 48 and ascii < 58))):
                result = False
                break
            else:
                if(letter == 'a' or letter =='e' or letter =='i' or letter == 'o' or letter == 'u' or letter == 'A' or letter =='E' or letter =='I' or letter == 'O' or letter == 'U'):
                    hasVowel = True
                else:
                    if((not hasCon) and not (ascii >= 48 and ascii < 58)):
                        hasCon = True

        if(not hasVowel or (not hasCon)):
            return False
        return result
