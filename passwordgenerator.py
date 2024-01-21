import random
l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
N = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("welcome to password generator")
letters=int(input("how many letters do you want in password"))
symbols=int(input("how many synmbols do you want in password"))
numbers=int(input("how many numbers do you want in password"))
password=""
for i in range (1,letters+1):
    c=random.choice(l)
    password+=c
for i in range (1,symbols+1):
    c=random.choice(s)
    password+=c
for i in range (1,numbers+1):
    c=random.choice(N)
    password+=c
p = list(password)
random.shuffle(p)
pas=""
for i in p:
    pas+=i
print(pas)