class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        def backtrack(charMap, count, path):
            if count == 0:
                res.add("".join(path))
                return
            res.add("".join(path))
            for key in charMap:
                if charMap[key] == 0: continue
                charMap[key] -= 1
                if charMap[key] == 0:
                    count -= 1
                path.append(key)
                backtrack(charMap, count, path)
                charMap[key] += 1
                if charMap[key] == 1:
                    count += 1
                path.pop()

        charMap = Counter(tiles)
        backtrack(charMap, len(charMap), [])
        return len(res) - 1