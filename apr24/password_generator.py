import random, string

length = 8
password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
print(password)