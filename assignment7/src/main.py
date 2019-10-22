import random
import numpy as np

print('Please input the times you want to play the game:')
num = int(input())
time_list = []
for i in range(num):
    coin = 10
    time = 0
    while coin > 0:
        coin -= 1
        time += 1
        wheel1 = random.randint(0, 3)
        wheel2 = random.randint(0, 3)
        wheel3 = random.randint(0, 3)
        if wheel1==0 and wheel2==0 and wheel3==0:
            coin+=20
        if wheel1==1 and wheel2==1 and wheel3==1:
            coin+=15
        if wheel1==2 and wheel2==2 and wheel3==2:
            coin+=5
        if wheel1==3 and wheel2==3 and wheel3==3:
            coin+=3
        if wheel1==3 and wheel2==3 and wheel3!=3:
            coin+=2
        if wheel1==3 and wheel2!=3:
            coin+=1
    time_list.append(time)
    print('Time',i+1,' number of plays:',time)
print('The mean number of plays: ',np.mean(time_list))
print('The median number of play: ',np.median(time_list))