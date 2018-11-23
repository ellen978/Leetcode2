'''
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).

Note:

There are at least 3 and at most 10,000 points.
Coordinates are in the range -10,000 to 10,000.
You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other. 

Example 1:

[[0,0],[0,1],[1,1],[1,0]]

Answer: True

Example 2:

[[0,0],[0,10],[10,10],[10,0],[5,5]]

Answer: False
'''

class Solution:
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points)<=4:
            return True
        else:
            points.append(points[0])
            points.insert(0,points[-2])
            i=1
            cross_product=[0]
            while i<len(points)-1:
                if (points[i][0]-points[i-1][0])*(points[i+1][1]-points[i][1])-(points[i][1]-points[i-1][1])*(points[i+1][0]-points[i][0]) !=0:
                    cross_product.append((points[i][0]-points[i-1][0])*(points[i+1][1]-points[i][1])-(points[i][1]-points[i-1][1])*(points[i+1][0]-points[i][0]))
                    if cross_product[-1]*cross_product[-2]<0:
                        return False
                    else:
                        i+=1
                else:
                    i+=1
            return True
