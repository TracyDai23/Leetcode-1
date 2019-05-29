'''
75%
Bottom-up adding
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        small = triangle[-1]
        
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                small[j] = min(small[j], small[j+1]) + triangle[i][j]
                
        return small[0]
