class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        self.bound = sum(w)

        for num in w:
            if not self.prefix:
                self.prefix.append([0, num])
            else:
                self.prefix.append([self.prefix[-1][1]+1, num + self.prefix[-1][1]])


    def pickIndex(self) -> int:
        picked_num = random.uniform(0, self.bound)
        # find the location of picked_num using binary search
        left, right = 0, len(self.prefix) - 1

        while left < right:
            mid = left + (right-left)//2

            if picked_num > self.prefix[mid][1]:
                left = mid + 1
            else:
                right = mid
                
        return left



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()