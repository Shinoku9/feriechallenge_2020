import string
import secrets
import pyperclip

char_base = string.ascii_letters + string.digits
pwd_length = int(input("Enter length of your password: "))

while True:
    password = ''.join(secrets.choice(char_base) for i in range(pwd_length))
    if (any(c.islower() for c in password) and any(c.isupper() for c in password) and sum(c.isdigit() for c in password) >= 1):
        break

pyperclip.copy(password)
print("Your password is: " + password)
