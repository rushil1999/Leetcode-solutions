import ("fmt")


func isPalindrome(left int, right int, s string, count int ) bool {
    if left >= right {
        return true
    } else {
        if s[left] == s[right] {
            return isPalindrome(left+1, right-1, s, count)
        } else {
            if(count > 1) {
                return false
            }
            leftSide := isPalindrome(left+1, right, s, count+1)
            rightSide := isPalindrome(left, right-1, s, count+1)
            return leftSide || rightSide
        }
    }
    
}
func validPalindrome(s string) bool {
    val:= isPalindrome(0, len(s)-1, s, 1)
    fmt.Println(val)
    return val
}