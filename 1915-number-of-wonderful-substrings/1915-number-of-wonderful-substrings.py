class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024
        count[0] = 1 
        bitmask = 0  
        result = 0  
        
        for char in word:
            char_index = ord(char) - ord('a')
            
            # Toggle the bit corresponding to the current character in the bitmask
            bitmask ^= 1 << char_index
            result += count[bitmask]
            
            for i in range(10):
                result += count[bitmask ^ (1 << i)]
            
            count[bitmask] += 1
        
        return result