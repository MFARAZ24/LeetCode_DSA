class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start,end = -1,-1
        left,right = 0,len(nums)-1

        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                start = mid
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
            else:
                right = right - 1
        left, right = 0,len(nums)-1

        while right>=left:
            mid = (left+right)//2
            if nums[mid] == target:
                end = mid
                left = mid+1
            elif nums[mid]>target:
                right =mid-1
            else:
                left = left+1
        return [start,end]
            

        