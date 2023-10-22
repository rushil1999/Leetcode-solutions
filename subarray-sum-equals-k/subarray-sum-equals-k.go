import ("fmt")

func subarraySum(nums []int, k int) int {
    size := len(nums)
    ans := 0
    sumMap := make(map[int]int)
    prefixSum := make([]int, size)
    currentSum := 0
    for i:= 0 ; i < size;i++ {
        currentSum += nums[i]
        prefixSum[i] = currentSum
        
        targetSum := currentSum - k
        fmt.Println(targetSum, sumMap[targetSum])
        ans += sumMap[targetSum]
        if currentSum == k {
            ans += 1
        }
        sumMap[currentSum] += 1
    }
//     fmt.Println(prefixSum)
//     for i:=0;i<size;i++ {
//         currentPrefixSum := prefixSum[i]
        
    // }
    return ans
    
}