class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        arr = []
        for key in count:
            arr.append(count[key])
        
        arr.sort(reverse=True)
        res = 0
        for i in range(len(arr)):
            if i < 8:
                res += arr[i]
            elif i < 16:
                res += (arr[i] * 2)
            elif i < 24:
                res += (arr[i] * 3)
            else:
                res += (arr[i] * 4)

        return res