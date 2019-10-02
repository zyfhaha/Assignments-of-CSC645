import random
from Map import Map
from Back_tracking import Back_tracking
from Back_forward import Back_forward
from Back_AC3 import Back_AC3
from Min_conflict import Min_conflict

print('Which problem do you want to solve?(usa or sudoku):')
pb=input()
if pb=='usa':
    print('Which map do you want to search?(10/51):')
    num_state = int(input())
    map = Map('us_states_' + str(num_state) + '_ij.txt')
    start_step=0
    print('Which algorithm do you want to use?(0/1/2/3)')
    print('0--pure back-tracking')
    print('1--back-tracking with forward-check')
    print('2--back-tracking with AC3')
    print('3--Min-conflict search')
    pn=int(input())
    if pn==3:
        Min_conflict(map)
        exit()
    print('Which method do you want to use?(0/1/2):')
    print('0--None')
    print('1--Degree heuristic')
    print('2-MRV')
    s_type=int(input())
    print('Do you want to use LCV?(Y/N)')
    if input()=='Y':
        lcv=1
    else:
        lcv=0
    print('Do you want a initial assignment for one state?(Y/N)')
    if input()=='Y':
        map.colors[0]=random.randint(0, 3)
        map.visited[0]=1
        start_step=1
    if pn==3:
        Min_conflict(map)
    if pn==0:
        if num_state==51:
            print('It will take a long time(about 5 minutes), do you want to wait(Y/N):')
            if input()=='N':
                exit()
        Back_tracking(map,start_step,s_type,lcv)
    if pn==1:
        Back_forward(map,start_step,s_type,lcv)
    if pn==2:
        Back_AC3(map,start_step,s_type,lcv)
