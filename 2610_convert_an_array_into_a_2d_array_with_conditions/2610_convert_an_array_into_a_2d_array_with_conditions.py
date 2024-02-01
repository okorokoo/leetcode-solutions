class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        arr = []
        while nums:
            arr.append(list(set(nums)))
            for i in arr[len(arr)-1]:
                nums.remove(i)
        return arr