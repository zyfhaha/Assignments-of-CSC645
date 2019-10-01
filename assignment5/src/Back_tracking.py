def Back_tracking(map,step):
    location=-1
    if step==len(map.states):
        if map.isgoal() == 1:
            map.picprint()
            map.textprint()
            exit()
        else:
            return 0
    else:
        for i in range(len(map.states)):
            if map.visited[i]==0:
                location=i
                break
        map.visited[location]=1
        for i in range(len(map.datalist[location])):
            map.colors[location]=map.datalist[location][i]
            Back_tracking(map,step+1)
        map.visited[location]=0
    return 0