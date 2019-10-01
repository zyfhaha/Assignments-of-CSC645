def Back_forward(map,step):
    location=-1
    if step==len(map.states):
        if map.isgoal() == 1:
            map.picprint()
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
            flaglist=[]
            b_flag=0
            for j in range(len(map.neighbour[location])):
                if map.datalist[location][i] in map.datalist[map.neighbour[location][j]]:
                    flaglist.append(1)
                    t=map.datalist[map.neighbour[location][j]].index(map.datalist[location][i])
                    map.datalist[map.neighbour[location][j]].pop(t)
                    if len(map.datalist[map.neighbour[location][j]])==0:
                        b_flag=1
                        break
                else:
                    flaglist.append(0)
            if b_flag==0:
                Back_forward(map,step+1)
            for j in range(len(flaglist)):
                if flaglist[j]==1:
                    map.datalist[map.neighbour[location][j]].append(map.datalist[location][i])
        map.visited[location]=0
    return 0