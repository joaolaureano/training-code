class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        found_characters = set()
        max_length = 0
        start = 0
        finish = 0

        while finish < len(s):
            character = s[finish]
            while(character in found_characters):
                found_characters.remove(s[start])
                start = start + 1
            found_characters.add(character)
            finish = finish + 1
            max_length = max(max_length, finish - start)
    
        return max_length