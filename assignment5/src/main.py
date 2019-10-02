from Map import Map
from Back_tracking import Back_tracking
from Back_forward import Back_forward
from Back_AC3 import Back_AC3

print('Which map do you want to search?(10/51):')
num_state=int(input())
map = Map('us_states_'+str(num_state)+'_ij.txt')

Back_AC3(map,0)