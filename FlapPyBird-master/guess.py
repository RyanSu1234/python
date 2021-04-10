import random

ans = random.randint(1, 10000000)

for i in range(1, 10000000):
    print(i)
    if i == ans:
        print("yes!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        break