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
    print('Which algorithm do you want to use?(0/1/2/3)')
    print('0--pure back-tracking')
    print('1--back-tracking with forward-check')
    print('2--back-tracking with AC3')
    print('3--Min-conflict search')
    pn=int(input())
    if pn==3:


Min_conflict(map)