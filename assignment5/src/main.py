import random
import datetime
from Map import Map
from Sudoku import Sudoku
from Back_tracking import Back_tracking
from Back_forward import Back_forward
from Back_AC3 import Back_AC3
from Min_conflict import Min_conflict

print('Which problem do you want to solve?(usa or sudoku):')
pb = input()
if pb == 'usa':
    print('Which map do you want to search?(10/51):')
    num_state = int(input())
    map = Map('us_states_' + str(num_state) + '_ij.txt')
    start_step = 0
    print('Which algorithm do you want to use?(0/1/2/3)')
    print('0--pure back-tracking')
    print('1--back-tracking with forward-check')
    print('2--back-tracking with AC3')
    print('3--Min-conflict search')
    pn = int(input())
    if pn == 3:
        start = datetime.datetime.now()
        Min_conflict(map,start,0)
        exit()
    print('Which method do you want to use?(0/1/2):')
    print('0--None')
    print('1--Degree heuristic')
    print('2--MRV')
    s_type = int(input())
    print('Do you want to use LCV?(Y/N)')
    if input() == 'Y':
        lcv = 1
    else:
        lcv = 0
    print('Do you want a initial assignment for one state?(Y/N)')
    if input() == 'Y':
        map.colors[0] = random.randint(0, 3)
        map.visited[0] = 1
        start_step = 1
    if pn == 0:
        if num_state == 51:
            print('WARNING!!!!!It will take a long time(about few minutes), do you want to wait?(Y/N)')
            if input() == 'N':
                exit()
        start = datetime.datetime.now()
        Back_tracking(map, start_step, s_type, lcv, start)
    if pn == 1:
        start = datetime.datetime.now()
        Back_forward(map, start_step, s_type, lcv, start)
    if pn == 2:
        start = datetime.datetime.now()
        Back_AC3(map, start_step, s_type, lcv, start)

else:
    sudoku = Sudoku()
    print('Which algorithm do you want to use?(0/1/2/3)')
    print('0--pure back-tracking')
    print('1--back-tracking with forward-check')
    print('2--back-tracking with AC3')
    print('3--Min-conflict search')
    pn = int(input())
    if pn == 3:
        start = datetime.datetime.now()
        Min_conflict(sudoku,start,1)
        exit()
    print('Which method do you want to use?(0/1/2):')
    print('0--None')
    print('1--Degree heuristic')
    print('2--MRV')
    s_type = int(input())
    print('Do you want to use LCV?(Y/N)')
    if input() == 'Y':
        lcv = 1
    else:
        lcv = 0

    if pn == 0:
        start = datetime.datetime.now()
        Back_tracking(sudoku, 0, s_type, lcv, start)
    if pn == 1:
        start = datetime.datetime.now()
        Back_forward(sudoku, 0, s_type, lcv, start)
    if pn == 2:
        start = datetime.datetime.now()
        Back_AC3(sudoku, 0, s_type, lcv, start)
