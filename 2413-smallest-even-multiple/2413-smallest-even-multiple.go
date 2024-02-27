func smallestEvenMultiple(n int) int {
    var i int = 1

    for {
        if i % 2 == 0 && i % n == 0 {
            return i
        }

        i++
    }
}