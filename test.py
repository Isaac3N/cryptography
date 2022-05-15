import hashlib

# initializing string
str = "Angie pays Christina 20 dollars"

# encoding  Angie pays Christina 20 dollars using encode()
# then sending to SHA256()
result = hashlib.sha256(str.encode())

# printing the equivalent hexadecimal value.
print("The sha256 encoded message is : ")
print(result.hexdigest())
