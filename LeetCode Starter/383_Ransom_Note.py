class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            magIndex = magazine.find(ransomNote[i])
            if magIndex == -1:
                return False
            magazine = magazine[0:magIndex] + magazine[magIndex + 1:]
        return True