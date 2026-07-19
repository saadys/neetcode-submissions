
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while l <= r:
            mid = int(r + l)//2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid 
        return -1









# complexity : O(n)
#class Solution:
#    def search(self, nums: List[int], target: int) -> int:
#
#        for i in range(0,len(nums)):
#            if nums[i]== target:
#                return i 
#        return -1
        