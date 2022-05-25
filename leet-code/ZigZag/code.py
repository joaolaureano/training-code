class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        all_strings = [] * numRows


        for index in range(len(s)):
            index_2 = index
            for index_2 in range(index, index + numRows):
                print(s[index_2])

            print(index_2)

            for index_2 in range(index_2 + 1 , numRows -1 1):
                print(s[index_2])

            print(index_2)

            break



Solution().convert("PAYPALISHIRING", 3)