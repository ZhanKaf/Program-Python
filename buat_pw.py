import random
element="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang=input("Berapa panjang kata sandi yang ingin anda buat?")
pw=""
for i in range(int(panjang)):
    pw += random.choice(element)
print(pw)
