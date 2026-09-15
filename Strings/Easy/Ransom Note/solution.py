class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = {}

        for char in magazine:
            if char in count:
                count[char] += 1

            else:
                count[char] = 1

        for ran in ransomNote:
            if ran not in count or count[ran] == 0:
                return False

            count[ran] -= 1

        return True

