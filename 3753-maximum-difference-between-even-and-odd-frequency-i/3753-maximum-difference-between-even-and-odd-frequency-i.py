class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        mxOdd, mxEven = 0, float("inf")

        for key in count:
            if count[key] & 1:
                mxOdd = max(mxOdd, count[key])
            else:
                mxEven = min(mxEven, count[key])
        
        return mxOdd - (mxEven if mxEven != float("inf") else 0)