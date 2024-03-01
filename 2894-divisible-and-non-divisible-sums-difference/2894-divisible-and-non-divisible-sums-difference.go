func differenceOfSums(n int, m int) int {
    num1 := 0
    num2 := 0

    i := 1
    for i < n + 1 {
        if i % m != 0 {
            num1 += i
        } else {
            num2 += i
        }

        i ++
    }   

    return num1 - num2
}