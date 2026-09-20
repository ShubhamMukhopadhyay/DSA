class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 0
        sign = 1

        if x < 0:
            sign = -1 
            x = -x

        while x > 0:
            d = x % 10
            s = s*10 + d
            x = x // 10

        s = s * sign

        if s < -2147483647 or s > 2147483647:
            return 0

        return s