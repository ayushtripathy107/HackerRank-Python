class Solution {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        // Initialize the first row with 1s because there's only 1 way to reach any cell in the first row
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
        }
        
        // Update the DP array for the remaining rows
        for (int r = 1; r < m; r++) {
            for (int c = 1; c < n; c++) {
                dp[c] += dp[c - 1]; // current cell = top cell + left cell
            }
        }
        
        return dp[n - 1];
    }
}
