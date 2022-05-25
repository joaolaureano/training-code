class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        is_signed = (dividend < 0) ^ (divisor < 0)
        carry = 0
        
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 1:
            carry = dividend
        else:
            for i in range(31,-1,-1) :
                if divisor << i <= dividend: # If divisor multiplied by 2 power of i is BIGGER or EQUAL to  dividend, then is DIVISIBLE
                    dividend -= divisor  << i 
                    carry +=  1 << i
        
        if is_signed:
            carry = carry * -1       
            
        if carry > 2 ** 31 - 1:
            carry = 2 ** 31 -1
            
        if carry < -2 ** 31:
            carry = -2 ** 31
        
        return carry


Solution().convert("PAYPALISHIRING", 3)