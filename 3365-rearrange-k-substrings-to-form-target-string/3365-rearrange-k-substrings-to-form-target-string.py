class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        words = defaultdict(int)

        i = 0
        while i < n:
            words[s[i:i+(n // k)]] += 1
            i += (n // k)

        i = 0
        while True:
            start = i

            for word in words:
                if words[word] < 1:
                    continue
                if word == t[i:i+len(word)]:
                    i += len(word)
                    words[word] -= 1
            if i == start:
                return False
            if i >= len(t):
                return True