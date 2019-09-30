from Map import Map

map = Map('us_states_51_ij.txt')

for i in range(len(map.states)):
    print(map.states[i])