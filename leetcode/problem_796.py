### Problem 796: Rotate String (Easy): https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in goal+goal

class Solution2:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s) != len(goal)):
            return False

        anas = []
        start = s
        rotated = ''
        while(rotated != s):
            rotated = start[1::] + start[0]
            anas.append(rotated)
            start = rotated

        for a in anas:
            if(a == goal):
                return True
        return False