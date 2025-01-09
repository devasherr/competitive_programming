func maxSubarraySumCircular(nums []int) int {
    gMax, gMin := nums[0], nums[0]
    maxSum, minSum := 0, 0
    total := 0

    for i := 0; i < len(nums); i++ {
        if maxSum < 0 {
            maxSum = 0
        }
        if minSum > 0 {
            minSum = 0
        }

        total += nums[i]
        maxSum += nums[i]
        minSum += nums[i]

        if maxSum > gMax {
            gMax = maxSum
        }
        if minSum < gMin {
            gMin = minSum
        }
    }

    if gMax < 0 {
        return gMax
    }
    if gMax > total - gMin {
        return gMax
    } else {
        return total - gMin
    }
}