class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cursum = 0
        runningSumList = nums
        for i in range(len(nums)):
            cursum += nums[i]
            runningSumList[i] = cursum
        return runningSumList