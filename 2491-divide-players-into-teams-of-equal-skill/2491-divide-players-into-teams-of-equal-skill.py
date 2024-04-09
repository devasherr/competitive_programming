class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l, r = 0, len(skill) - 1
        skill.sort()
        res = 0
        prevSum = skill[l] + skill[r]

        while l < r:
            if skill[l] + skill[r] != prevSum:
                return -1

            res += (skill[l] * skill[r])
            
            l += 1
            r -= 1
        
        return res