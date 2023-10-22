import ("fmt")

func findPeak(nums []int, left int, right int) int {
    size := len(nums)
    mid := (left+right)/2
    if left > right {
         return -1
    }
    if mid-1 >=0 && nums[mid] < nums[mid-1]  {
        return mid
    } else if mid+1 < size && nums[mid] > nums[mid+1] {
        return mid+1
    }
    leftSideIndex := findPeak(nums, left, mid-1)
    rightSideIndex := findPeak(nums, mid+1, right)

    if leftSideIndex > -1 {
        return leftSideIndex
    }
    if rightSideIndex > -1 {
         return rightSideIndex
    } 
    return -1
}
func seachInSortedArray(nums []int, left int, right int, target int) int {
    for left <= right {
        mid := (left + right)/2
        if nums[mid] == target {
            return mid
        } else if nums[mid] > target {
            right = mid-1
        } else {
            left = mid+1
        }
    }
    return -1
}


func search(nums []int, target int) int {
    size := len(nums)
    peakIndex := findPeak(nums, 0, size-1)
    fmt.Println(peakIndex)
    if peakIndex == -1 {
        case1 :=  seachInSortedArray(nums, 0, size-1, target)
        return case1
    } else {
        case1 :=  seachInSortedArray(nums, 0, peakIndex-1, target)
        case2 :=  seachInSortedArray(nums, peakIndex, size-1, target)
        if case1 > -1 {
        return case1
        } else if case2 > -1 {
            return case2
        } 
    }
    
    return -1
}