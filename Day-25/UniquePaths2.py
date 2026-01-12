class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Create dp table
        dp = [[0]*n for _ in range(m)]
        
        # Initialize start position
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            return 0  # If start itself is an obstacle
        
        # Fill first column
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0
        
        # Fill first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = 0
        
        # Fill rest of the table
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        
        return dp[m-1][n-1]

# Example usage:
grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

sol = Solution()
print(sol.uniquePathsWithObstacles(grid))  # Output: 2