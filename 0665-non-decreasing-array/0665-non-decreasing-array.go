func checkPossibility(nums []int) bool {
    changed := false
    for i := 1; i < len(nums); i++ {
        if nums[i-1] <= nums[i] {
            continue
        }

        if changed {
            return false
        }
        if i == 1 || nums[i-2] <= nums[i] {
            nums[i-1] = nums[i]
        } else {
            nums[i] = nums[i-1]
        }
        changed = true
    }   

    return true 
}