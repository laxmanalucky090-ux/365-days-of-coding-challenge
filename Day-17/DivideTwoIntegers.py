class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign
        negative = (dividend < 0) ^ (divisor < 0)

        # Use absolute values
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        # Main loop
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Double temp until it exceeds dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            result += multiple

        # Apply sign
        if negative:
            result = -result

        # Clamp to 32-bit range
        return max(INT_MIN, min(INT_MAX, result))