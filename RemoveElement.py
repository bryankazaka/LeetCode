class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for x in nums:
            if x!= val:
                nums[counter]=x
                counter+=1
        return counter
        
