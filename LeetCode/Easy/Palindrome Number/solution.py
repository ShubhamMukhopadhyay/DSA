class Solution(object):
    def isPalindrome(self, x):
        # temp = x
        # reversed_num = 0

        # while temp > 0 :
        #     r = temp % 10
        #     temp//=10
        #     reversed_num = reversed_num * 10 + r 

        # if reversed_num == x:
        #     return True

        # else:
        #     return False 

        temp = x
        reverse = 0

        while temp>0:
            r = temp % 10
            temp //= 10
            reverse = reverse*10+r

        if reverse == x:
            return True

        else:
            return False