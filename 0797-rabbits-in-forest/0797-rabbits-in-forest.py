class Solution:
    def numRabbits(self, answers) -> int:
        answers.sort()
        i, res = 0, 0

        while i < len(answers):
            for _ in range(answers[i]):
                if i + 1 >= len(answers): break
                if answers[i] != answers[i+1]: break
                i += 1
            
            res += answers[i] + 1
            i += 1
        return res