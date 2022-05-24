class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = int(('-' + str(x)[1:][::-1]) if x < 0 else str(x)[::-1])
        return result if -2 ** 31 < result < (2 ** 31 -1 ) else 0
        

print(Solution().reverse(1534236469))