'''
Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
'''

'''
Solution 1
'''
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        return sorted(a*x**2+b*x+c for x in nums)

'''
Solution 2
'''

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        result=[a*nums[0]**2+b*nums[0]+c]
        pos=0
        i=1
        while i<len(nums):
            r=a*nums[i]*nums[i]+b*nums[i]+c
            while pos>0 and r<result[pos]:
                pos-=1
            while pos<i and r>result[pos]:
                pos+=1
            result.insert(pos,r)
            i+=1
        return result
