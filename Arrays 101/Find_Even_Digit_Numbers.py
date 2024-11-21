class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evenCount = 0
        for num in nums:
            curCount = 1
            while (num >= 10):
                curCount += 1
                num = num // 10
            if curCount % 2 == 0:
                evenCount += 1
        return evenCount