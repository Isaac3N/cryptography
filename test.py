import hashlib

# initializing string
str = "Angie pays Christina 20 dollars"

# encoding  Angie pays Christina 20 dollars using encode()
# then sending to SHA256()
result = hashlib.sha256(str.encode())

# printing the equivalent hexadecimal value.
print("The sha256 encoded message is : ")
print(result.hexdigest())


# Expected Output:
# The sha256 encoded message is : 29fcf5b89c8adcb6e757582a4a0b3f8ad2c2550f5fde94a3f1cea1dedd0a4c4d
