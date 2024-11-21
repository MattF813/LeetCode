class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newNums = [0]*len(nums)
        for i in range(len(nums)):
            newNums[i] = nums[i] * nums[i]
        newNums.sort()
        return newNums