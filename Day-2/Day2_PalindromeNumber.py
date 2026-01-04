
x = int(input("Enter a number: "))

rev = 0
original = x

# Reverse the number
while x > 0:
    digit = x % 10
    rev = rev * 10 + digit
    x //= 10

# Check if palindrome
if original == rev:
    print(f"{x} is a Palindrome")
else:
    print(f"{x} is not a Palindrome")