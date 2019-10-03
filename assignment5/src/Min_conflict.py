import random
import datetime

def Min_conflict(map):
    for i in range(len(map.colors)):
        if map.visited[i] == 0:
            map.colors[i] = random.randint(1, 9)
    step = 0
    goal_flag = map.isgoal()
    while goal_flag == 0 and step < 100000:
        i = random.randint(0, len(map.colors) - 1)
        if map.visited[i] == 1:
            continue
        conflictlist = []
        for j in range(len(map.datalist[i])):
            con_sum = 0
            for k in range(len(map.neighbour[i])):
                if map.datalist[i][j] == map.colors[map.neighbour[i][k]]:
                    con_sum += 1
            conflictlist.append((con_sum))
        ind = conflictlist.index(min(conflictlist))
        map.colors[i] = map.datalist[i][ind]
        goal_flag = map.isgoal()
        step += 1
    if map.isgoal() == 1:
        map.textprint()
        map.picprint()
    else:
        print('Failed, can not find a answer! The final state will show later.')
        map.picprint()
