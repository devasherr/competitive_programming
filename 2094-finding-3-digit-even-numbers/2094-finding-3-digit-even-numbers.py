class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # lord what have i done :'(

        res = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and j != k and k != i:
                        val = 0
                        for n in [digits[i], digits[j], digits[k]]:
                            val *= 10
                            val += n
                        if 100 <= val <= 999 and val % 2 == 0:
                            res.add(val)
        return sorted(list(res))