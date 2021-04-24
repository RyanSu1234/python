import random

def roll_dice(n):
    dice=[]
    for i in range(n):
        dice.append(random.randint(1,600))#隨機取整數(???~???)
    return dice

num_dice = int(input('n'))

new_list=roll_dice(num_dice)

print(new_list)

