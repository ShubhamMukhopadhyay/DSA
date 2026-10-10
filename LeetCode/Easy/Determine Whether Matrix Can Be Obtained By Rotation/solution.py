class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        n = len(mat)

        for rotation in range(4):
            if mat == target:
                return True

            for i in range(n):
                for j in range(i+1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for row in mat:
                row.reverse()

        return False