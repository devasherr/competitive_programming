func longestCommonSubsequence(text1 string, text2 string) int {
    var dp = make([][]int, len(text1) + 1)
    for i := range dp {
        dp[i] = make([]int, len(text2) + 1)
    }

    for i := 1; i < len(dp); i++ {
        for j := 1; j < len(dp[0]); j++ {
            ix, jx := i-1, j-1
            if text1[ix] != text2[jx] {
                dp[i][j] = maxInt(dp[i][j-1], dp[i-1][j])
            } else {
                dp[i][j] = dp[i-1][j-1] + 1
            }
        }
    }

    return dp[len(dp) - 1][len(dp[0]) - 1]
}

func maxInt(x, y int) int {
    if x > y {
        return x
    }
    return y
}