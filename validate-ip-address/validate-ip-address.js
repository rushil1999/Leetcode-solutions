/**
 * @param {string} queryIP
 * @return {string}
 */

const isValidIPV4 = (ip) => {
    const ipElements = ip.split(".")
    if(ipElements.length !== 4){
        return false
    }
    let isValidIpv4 = true
    ipElements.forEach((element) => {
        if(element[0] === "0" && element.length > 1){
            isValidIpv4 = false
            return
        }    
        isInteger = /^\d+$/.test(element) 
        if(isInteger === false){
            isValidIpv4 = false
            return
        }
        
        let num = parseInt(element)
        console.log(element, num)
        if(num < 0 || num > 255){
            isValidIpv4 = false
            return
        }
    })
    console.log("checking for..", ip, isValidIpv4)
    return isValidIpv4
    
}

const isValidIPV6 = (ip) => {
    const ipElements = ip.split(":")
    if(ipElements.length !== 8){
        return false
    }
    let isValidIpv6 = true
    ipElements.forEach((element) => {
        if(element.length > 4 || element.length < 1){
            isValidIpv6 = false
            return
        }
       Array.from(element).forEach((ch) => {
           let lowerCasedChar = ch.toLowerCase() 
           // console.log(ch, lowerCasedChar)
           if(!/^\d+$/.test(lowerCasedChar) && (lowerCasedChar > 'f' || lowerCasedChar < 'a')){
               console.log(ch, lowerCasedChar)
               isValidIpv6 = false
               return false
           }
       })

    })
    return isValidIpv6
}

var validIPAddress = function(queryIP) {
    
    if(isValidIPV4(queryIP)){
        return "IPv4"
    }
    
    if(isValidIPV6(queryIP) === true){
        return "IPv6"
    }
    return "Neither"
    
};