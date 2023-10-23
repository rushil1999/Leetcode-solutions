func recurse(nums []int, left int, right int ) int {
    size := len(nums)
    if left > right {
         return -1
    } 
    mid := (left + right)/2
    if mid-1 >=0 && nums[mid] > nums[mid-1] && mid+1 < size && nums[mid] > nums[mid+1] {
        return mid
    } else if mid == 0 && mid+1 < size && nums[mid] > nums[mid+1] {
        return mid
    } else if mid == size-1 && mid-1 >= 0 && nums[mid] > nums[mid-1] {
        return mid
    } else if mid-1 ==0 && mid+1 >= size {
        return mid
    } 
    case1 := recurse(nums, left, mid-1)
    case2 := recurse(nums, mid+1, right)
    
    if case1 > -1 {
        return case1
    } 
    if case2 > -1 {
        return case2
    } 
    
    return -1
}


func findPeakElement(nums []int) int {
    if len(nums) == 1{
        return 0
    }
    peakIndex := recurse(nums, 0, len(nums)-1)
    return peakIndex
}