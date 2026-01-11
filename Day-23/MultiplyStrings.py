class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If one of them is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize result array
        m, n = len(num1), len(num2)
        result = [0] * (m + n)  # max length of product = m+n

        # Reverse iterate both strings
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                sum_ = mul + result[i + j + 1]  # add existing value
                result[i + j + 1] = sum_ % 10  # place digit
                result[i + j] += sum_ // 10    # carry

        # Convert result array to string
        res_str = "".join(map(str, result))
        
        # Remove leading zeros
        return res_str.lstrip("0")