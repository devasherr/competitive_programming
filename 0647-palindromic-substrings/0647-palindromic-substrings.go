func countSubstrings(s string) int {
    checkPalindrome := func(i, j int) int {
        cur := 0
            for i >= 0 && j < len(s) && s[i] == s[j] {
                cur += 1
                i--
                j++
            }

        return cur
    }

    res := 0
    for i := 0; i < len(s) - 1; i++ {
        res += checkPalindrome(i, i)
        res += checkPalindrome(i, i+1)
    }

    // don't forget the last character
    return res + 1
}