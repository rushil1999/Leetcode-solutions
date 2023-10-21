/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var lengthOfLongestSubstringKDistinct = function(s, k) {
    
    let left = 0
    let right = 0
    
    let charCount = s.length
    let maxSubStringLength = 0
    charMap = new Map()
    while(right < charCount && left <= right){
        let currentCharacter = s[right]
        if (charMap.get(currentCharacter) === undefined){
            charMap.set(currentCharacter, 1)
        }
        else{
            charMap.set(currentCharacter, charMap.get(currentCharacter)+1)
        }
        
        while(charMap.size > k && left <= right ){
            leftMostCharacter = s[left]
            charMap.set(leftMostCharacter, charMap.get(leftMostCharacter)-1)
            if(charMap.get(leftMostCharacter) === 0){
                charMap.delete(leftMostCharacter)
            }
            left += 1
        }
        maxSubStringLength = Math.max(maxSubStringLength, right -left+1)
        // console.log(left, right, currentCharacter, charMap, charMap.size, maxSubStringLength)
        
        right += 1
    }
    return maxSubStringLength
    
};