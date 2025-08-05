class Solution:
    def numOfUnplacedFruits(self, fruits, baskets) -> int:
        res = 0
        
        for i in range(len(fruits)):
            found = False
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i]:
                    baskets[j] = 0
                    res += 1
                    break

        return len(fruits) - res
