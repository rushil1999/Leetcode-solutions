import ("sort" 
        "fmt"
       "strings")

func groupAnagrams(strs []string) [][]string {
    wordMap := make(map[string][]string)
    for _, word := range strs {
        chars := strings.Split(word, "")
        sort.Strings(chars)
        sortedWord := strings.Join(chars, "")
        wordMap[sortedWord] = append(wordMap[sortedWord], word)
    } 
    fmt.Println(wordMap)
    var ans [][]string
    for _, value := range wordMap{
        ans = append(ans, value)
    }
    return ans
}