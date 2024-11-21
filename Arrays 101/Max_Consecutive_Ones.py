class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        onesCount = 0
        curCount = 0
        for num in nums:
            if num == 1:
                curCount += 1
            else:
                if curCount > onesCount:
                    onesCount = curCount
                curCount = 0
        if curCount > onesCount:
            onesCount = curCount
        return onesCount