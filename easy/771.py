"""
https://leetcode-cn.com/problems/jewels-and-stones/
"""

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0 
#       使用map进行标记,整体o(n)
        map = {}
        for i in J:
            map[i] = 1
        for i in S:
            if i in map:
                result = result + 1
        
        return result
              
        