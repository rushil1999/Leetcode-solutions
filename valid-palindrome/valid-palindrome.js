/**
 * @param {string} s
 * @return {boolean}
 */

const isAlphaNum = (char) => {
    return /^[a-zA-Z0-9]+$/.test(char);
}

var isPalindrome = function(s) {
    let parsedString = "";
    Array.from(s).forEach((char) => {
        if(isAlphaNum(char) === true){
            parsedString += char.toLowerCase()
        }
    })
    
    let left = 0
    let right = parsedString.length-1
    
    while(left <= right) {
        if(parsedString[left] != parsedString[right]){
            return false
        }
        else{
            left += 1
            right -= 1
        }
    }
    return true
    
    
};