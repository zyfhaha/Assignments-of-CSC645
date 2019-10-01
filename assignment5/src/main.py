from Map import Map
from Back_tracking import Back_tracking

print('Which map do you want to search?(10/51):')
num_state=int(input())
map = Map('us_states_'+str(num_state)+'_ij.txt')

map.picprint()

Back_tracking(map,0)