def Back_forward(map,step, s_type):
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
            del_index=[]
            del_color=[]
            map.colors[location] = map.datalist[location][i]
            isaviliable = 1
            for j in range(len(map.neighbour[location])):
                if map.visited[map.neighbour[location][j]] != 0 and map.colors[map.neighbour[location][j]] == \
                        map.colors[location]:
                    isaviliable = 0
                if map.visited[map.neighbour[location][j]] == 0:
                    if map.colors[location] in map.datalist[map.neighbour[location][j]]:
                        dindex=map.datalist[map.neighbour[location][j]].index(map.colors[location])
                        map.datalist[map.neighbour[location][j]].pop(dindex)
                        if len(map.datalist[map.neighbour[location][j]]) == 0:
                            isaviliable = 0
                        del_index.append(map.neighbour[location][j])
                        del_color.append(map.colors[location])
            if isaviliable == 1:
                Back_forward(map, step + 1, s_type)
            for j in range(len(del_index)):
                map.datalist[del_index[j]].append(del_color[j])
        map.visited[location] = 0
        map.colors[location] = -1
    return 0