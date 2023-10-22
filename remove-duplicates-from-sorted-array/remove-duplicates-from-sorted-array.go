import ("fmt")

func removeDuplicates(nums []int) int {
    left := 0
    size := len(nums)
    current := nums[left]
    right := left + 1
    count := 1
    for right < size {
        if nums[right] != current {
            nums[left+1] = nums[right]
            count += 1
            left += 1
            current = nums[right]
        }
        right += 1
    }
    fmt.Println(nums)
    return count
    
}