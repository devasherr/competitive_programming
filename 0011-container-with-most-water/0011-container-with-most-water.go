func maxArea(height []int) int {
    res := 0
    left, right := 0, len(height) - 1

    for left < right {
        cur := (right - left) * min(height[left], height[right])
        if cur > res {
            res = cur
        }

        if height[left] < height[right] {
            left++
        } else {
            right--
        }
    }

    return res
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}