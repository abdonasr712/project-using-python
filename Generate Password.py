import random
passlen = int(input("enter the length of password : "))
x= "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
y = "".join(random.sample(x, passlen))
print(y)
