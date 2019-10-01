from Map import Map
from Back_tracking import Back_tracking
from Back_forward import Back_forward

print('Which map do you want to search?(10/51):')
num_state=int(input())
map = Map('us_states_'+str(num_state)+'_ij.txt')

Back_tracking(map,0)