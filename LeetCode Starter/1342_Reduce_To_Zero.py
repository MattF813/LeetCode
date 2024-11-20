class Solution:
    def numberOfSteps(self, num: int) -> int:
        stepCount = 0
        curNum = num
        while(curNum != 0):
            stepCount += 1
            if curNum % 2 == 0:
                curNum = curNum / 2
            else:
                curNum -= 1
        return stepCount