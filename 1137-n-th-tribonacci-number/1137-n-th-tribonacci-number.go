func tribonacci(n int) int {
    var arr = []int{0, 1, 1}
    curSum := 2

    for n > 0 {
        temp := arr[0]

        arr[0], arr[1], arr[2] = arr[1], arr[2], curSum
        curSum = curSum + curSum - temp
        n--
    }

    return arr[0]
}