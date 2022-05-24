class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        values_dict = set()
        for index in range(len(nums)):
            value = nums[index]
            complementary_value = target - value
            if not complementary_value in values_dict:
                values_dict.add(value)
                continue
            comp_index = nums.index(complementary_value)
            return [comp_index, index]
            
        return []