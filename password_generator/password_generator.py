import random

big_button = "QWERTYUIOPLKJHGFDSAZXCVBNM"
small_button = "qwertyuioplkjhgfdsazxcvbnm"
number = "1234567890"
symbols = "~!@#$%^&*()_+?><*/"


use = big_button + small_button + number + symbols
password_length = 8
pasword = "".join(random.sample(use,password_length))

print("your password is:  ",pasword)

#easy Peezy lemonsqueezy :)