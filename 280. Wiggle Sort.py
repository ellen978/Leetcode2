'''
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
'''

class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=2:
            nums.sort()
        k=0
        while 2*k+1<len(nums):
            if 2*k+2<len(nums):
                if nums[2*k+1]>=max(nums[2*k], nums[2*k+2]):
                    k+=1
                elif nums[2*k]>nums[2*k+2]:
                    nums[2*k],nums[2*k+1]=nums[2*k+1],nums[2*k]
                    k+=1
                else:
                    nums[2*k+1],nums[2*k+2]=nums[2*k+2],nums[2*k+1]
                    k+=1
            else:
                if nums[2*k+1]>=nums[2*k]:
                    k+=1
                else:
                    nums[2*k],nums[2*k+1]=nums[2*k+1],nums[2*k]
                    k+=1
