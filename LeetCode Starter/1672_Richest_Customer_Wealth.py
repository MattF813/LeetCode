class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richestwealth = 0
        for i in range(len(accounts)):
            currentwealth = 0
            for j in range(len(accounts[i])):
                currentwealth += accounts[i][j]
            if currentwealth > richestwealth:
                richestwealth = currentwealth
        return richestwealth