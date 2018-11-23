'''
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
'''

class Solution:
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        all_list=[y[i] for y in arrays for i in range(len(y))]
        max_all=max(all_list)
        min_all=min(all_list)
        index_max=[i for i in range(len(arrays)) if max_all in arrays[i]]
        index_min=[i for i in range(len(arrays)) if min_all in arrays[i]]
        if len(index_max)>1 or len(index_min)>1:
            return max_all-min_all
        else:
            index_max=[i for i in range(len(arrays)) if max_all in arrays[i]][0]
            index_min=[i for i in range(len(arrays)) if min_all in arrays[i]][0]
            if index_max!=index_min:
                return max_all-min_all
            else:
                arrays_no_max=[x for x in arrays if x!=arrays[index_max]]
                max_2=max([y[i] for y in arrays_no_max for i in range(len(y))])
                arrays_no_min=[x for x in arrays if x!=arrays[index_min]]
                min_2=min([y[i] for y in arrays_no_min for i in range(len(y))])
                return max([max_all-min_2,max_2-min_all])
