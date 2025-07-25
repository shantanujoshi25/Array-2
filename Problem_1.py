# // Time Complexity : O(n)
# // Space Complexity : O( 1)
    
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        for i in range(len(nums)):
            if(nums[i] > 0):
                output.append(i+1)
        return output