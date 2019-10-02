def Back_tracking(map, step, s_type, lcv):
    location = -1
    if step == len(map.states):
        if map.isgoal() == 1:
            map.picprint()
            map.textprint()
            exit()
        else:
            return 0
    else:
        for i in range(len(map.states)):
            if map.visited[i] == 0:
                location = i
                break
        if s_type==1:
            tt=location
            for i in range(tt,len(map.states)):
                if map.visited[i]==0 and map.num_neighbour[i]>map.num_neighbour[location]:
                    location=i
        if s_type==2:
            tt=location
            for i in range(tt,len(map.states)):
                if map.visited[i]==0 and len(map.datalist[i]) < len(map.datalist[location]):
                    location=i
        map.visited[location] = 1
        for i in range(len(map.datalist[location])):
            map.colors[location] = map.datalist[location][i]
            isaviliable = 1
            for j in range(len(map.neighbour[location])):
                if map.visited[map.neighbour[location][j]] != 0 and map.colors[map.neighbour[location][j]] == \
                        map.colors[location]:
                    isaviliable = 0
            if isaviliable == 1:
                Back_tracking(map, step + 1, s_type, lcv)
        map.visited[location] = 0
        map.colors[location] = -1
    return 0
