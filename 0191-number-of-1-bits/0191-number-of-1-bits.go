func hammingWeight(n int) int {
    res := 0
    for idx := 0; idx < 32; idx++ {
        if n & (1 << idx) != 0 {
            res++
        }
    }
    return res
}