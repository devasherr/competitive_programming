class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        arr = []

        for key in count:
            arr.append((count[key], key))
        
        arr.sort(reverse=True)
        res = []
        for count, char in arr:
            for _ in range(count):
                res.append(char)
        
        return "".join(res)