# Dice simulator
import numpy as np

dice=np.random.randint(1,7,10)
print(dice)
print(np.mean(dice))
print(np.size(dice[dice==6]))
print(dice[dice>3])
l=[]
for i in dice:
    if i not in l:
        print(i,":",np.size(dice[dice==i]))
    l.append(i)
l=np.unique(dice)
max_count=0
max_number=None
for i in l:
    n=np.size(dice[dice==i])
    if n>max_count:
        max_count=n
        max_number=i
print(max_number)
