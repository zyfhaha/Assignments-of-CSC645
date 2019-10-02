from Map import Map
from Back_tracking import Back_tracking
from Back_forward import Back_forward
from Back_AC3 import Back_AC3
from Min_conflict import Min_conflict

print('Which problem do you want to solve?(usa or sudu)')
print('Which map do you want to search?(10/51):')
num_state=int(input())
map = Map('us_states_'+str(num_state)+'_ij.txt')

Min_conflict(map)