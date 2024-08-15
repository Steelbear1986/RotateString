class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) > len(goal): return False
        for i in range(len(s)):
            if s[:i] in goal and s[i:] in goal:
                return True
        return False
