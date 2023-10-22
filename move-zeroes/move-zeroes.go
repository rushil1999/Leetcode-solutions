import ("fmt")

func moveZeroes(nums []int)  {
    size := len(nums)
    i := 0
    target := -1
    for i < size {
        if(nums[i] != 0 && target > -1 && target < i ) {
            nums[target] = nums[i]
            nums[i] = 0
            k:= target+1
            for k < size && nums[k] != 0 {
                k+=1
            }
            target = k
        } else if nums[i] == 0 {
            if target == -1 {
                target = i
            }
        }
        i += 1
    }
    fmt.Println(nums)
}