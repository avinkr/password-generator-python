import random 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number ="0123456789"
all = lower + upper + number
length = 8  #requred length
password = "" .join(random.sample(all, length))
print(password)