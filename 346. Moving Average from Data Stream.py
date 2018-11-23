'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''

class MovingAverage:
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.arr=[]
        self.size=size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.arr.insert(0,val)
        if len(self.arr)<self.size:
            return sum(self.arr)/len(self.arr)
        else:
            array=self.arr[:self.size]
            return sum(array)/self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
