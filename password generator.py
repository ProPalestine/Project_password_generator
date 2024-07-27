import random
import string

print("how much length your password you want")
pass_len = int(input())

charVal = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charVal)

print("your random password is ", password)

