'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
'''

class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr=[]

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.arr.append(number)
        
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        self.arr.sort()
        i,j=-0,len(self.arr)-1
        while i<j:
            if self.arr[i]+self.arr[j]==value:
                return True
            elif self.arr[i]+self.arr[j]<value:
                i+=1
            else:
                j-=1
        return False
