func maxSubArray(nums []int) int {
    res , curSum := math.MinInt16, 0

    for i := 0; i < len(nums); i++ {
        if curSum < 0 {
            curSum = 0
        }

        curSum += nums[i]
        if curSum > res {
            res = curSum
        }
    }   

    return res
}