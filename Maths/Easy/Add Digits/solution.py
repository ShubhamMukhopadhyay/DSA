class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) > 1:
            s = 0

            for digits in str(num):
                s += int(digits)
                
            num = s

        return num