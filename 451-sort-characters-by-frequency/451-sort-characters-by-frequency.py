class Solution:
    def frequencySort(self, s: str) -> str:
        frequencies = []
        frequencyMap = {}
        
        for character in s:
            if( character in frequencyMap):
                frequencyMap[character] += 1
            else:
                frequencyMap[character]  = 1
            
        for key in frequencyMap:
            frequencies.append((frequencyMap[key],key))
        frequencies.sort(key=lambda x: x[0], reverse=True)
        arr = ""
        
        print(frequencies)
        
        for (frequency, char) in frequencies:
            s = char*frequency
            arr+= s
        return arr