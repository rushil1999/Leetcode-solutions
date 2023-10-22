func checkMapping(sMap map[rune]int, tMap map[rune]int) bool { 
    
    for key, val := range tMap {
        if sMap[key] < val {
            return false
        }
    }
    return true
    
}




func minWindow(s string, t string) string {
    sMap := make(map[rune]int)
    tMap := make(map[rune]int)
    
    left := 0
    right := 0
    size := len(s)
    ans := ""
    
    
    for _, character := range t {
        tMap[rune(character)] += 1
    }
    
    for right < size {
        character := rune(s[right])
        sMap[character] += 1
        // val := checkMapping(sMap, tMap)
        // fmt.Println(string(character), val)
        if checkMapping(sMap, tMap) {
            for left <= right && checkMapping(sMap, tMap) {
                chacterToRemove := rune(s[left])
                sMap[chacterToRemove] -= 1
                left += 1
            }
            if right-(left-1)+1 < len(ans) || len(ans) == 0{
                ans = s[left-1:right+1]
            }
            
            // fmt.Println(left, right, ans, s[right], s[left-1:right+1])
        }
        right += 1
    }
    return ans
    
    
    
    
    
}