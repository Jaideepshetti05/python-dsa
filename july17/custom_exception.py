class AgeError(Exception):
    pass

def check(age):
    if age < 18:
        raise AgeError("Not Eligible")

try:
    check(16)
except AgeError as e:
    print(e)