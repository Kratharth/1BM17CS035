import string
from random import *
lis = string.ascii_letters + string.punctuation + string.digits
pwd = "".join(choice(lis) for i in range(randint(6,12)))
print('the password is : ',end = " ")
print(pwd)
