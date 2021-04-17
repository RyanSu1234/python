import random as r
print(r.randint(1,600000))
i = 4
x = 1
while i != 5:
    i = (int(r.randint(1,600000)))
    print(i)
    x = x + 1
else:
    print("YA")
    print('共抽了',x,'次')