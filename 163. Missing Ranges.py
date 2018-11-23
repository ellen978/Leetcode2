'''
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''

class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums=sorted(list(set(nums)))
        nums.insert(0,lower-1)
        nums.append(upper+1)
        output=[]
        i=0
        while i<len(nums)-1:
            if nums[i+1]==nums[i]+1:
                i+=1
            elif nums[i+1]==nums[i]+2:
                output.append(str(nums[i]+1))
                i+=1
            else:
                output.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))
                i+=1
        return output
