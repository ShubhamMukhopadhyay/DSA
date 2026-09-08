class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        result = []

        while i >= 0 or j >=0 or carry:
            if i >= 0:
                bit_a = int(a[i])
            else:
                bit_a = 0

            if j >= 0:
                bit_b = int(b[j])
            else:
                bit_b = 0

            total = bit_a + bit_b + carry

            digit_to_write = total % 2
            carry = total // 2

            result.append(str(digit_to_write))
            i -= 1
            j -= 1
        

        result.reverse()
        return "".join(result)