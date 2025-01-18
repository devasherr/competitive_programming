class Solution:
    def checkValid(self, arr, derived):
        for i in range(len(derived)):
            arr.append(arr[i] ^ derived[i])
        return arr[0] == arr[-1]

    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return self.checkValid([1], derived) or self.checkValid([0], derived)