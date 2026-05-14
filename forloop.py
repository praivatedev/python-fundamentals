for i in (0, 1, 2):
    print("meow!!")

#add range
for i in range(3):
    print("meow!!")

while True:
    n = int(input("What's n "))

    if n < 0:
        continue
    else:
        break

while True:
    p = int(input("What's p "))

    if p > 0:
        break;

for _ in range(p):
    print("meow!!!!")


#use functions for reusability

def main():
    meow(get_number());

def get_number():

    while True:
        x = int(input("What's x "))

        if x > 0:
            return x;

def meow(x):
    for _ in range(x):
        print("Moew!!")
    

main()
