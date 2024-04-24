func fib(n int) int {
    n1, n2 := 0, 1
    temp, curSum := 0, 1

    for n > 0 {
        temp = n2
        n1 = n2
        n2 = curSum

        curSum += temp
        n--
    }   

    return n1
}