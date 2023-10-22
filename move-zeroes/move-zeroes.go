import ("fmt")

func moveZeroes(nums []int)  {
    size := len(nums)
    i := 0
    target := -1
    for i < size {
        // fmt.Println("DA", nums[i], target, i)
        if(nums[i] != 0 && target > -1 && target < i ) {
            // fmt.Println("Caught", nums[i], target)
            nums[target] = nums[i]
            nums[i] = 0
            k:= target+1
            // fmt.Println("WHereada", k, nums[k])
            for k < size && nums[k] != 0 {
                k+=1
            }
            
            target = k
            // fmt.Println("New Target", target, i)
        } else if nums[i] == 0 {
            if target == -1 {
                target = i
            }
        }
        i += 1
    }
    fmt.Println(nums)
}