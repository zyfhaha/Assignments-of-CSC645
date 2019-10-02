class constraint:
    def __init__(self, l, r):
        self.l_point = l
        self.r_point = r


def remove(map, pi, pj, del_index, del_color):
    flag = 0
    isaviliable = 1
    rm_list = []
    for i in range(len(map.datalist[pi])):
        sum_p = 0
        for j in range(len(map.datalist[pj])):
            if map.datalist[pi][i] != map.datalist[pj][j]:
                sum_p += 1
        if sum_p == 0:
            flag = 1
            rm_list.append(map.datalist[pi][i])
            del_index.append(pi)
            del_color.append(map.datalist[pi][i])
    for i in range(len(rm_list)):
        ind = map.datalist[pi].index(rm_list[i])
        map.datalist[pi].pop(ind)
        if len(map.datalist[pi]) == 0:
            isaviliable = 0
    return flag, isaviliable


def AC3_check(map, del_index, del_color):
    flag = 1
    checklist = []
    for i in range(len(map.borders)):
        checklist.append(constraint(map.borders[i].index1, map.borders[i].index2))
        checklist.append(constraint(map.borders[i].index2, map.borders[i].index1))
    while len(checklist) != 0:
        cons = checklist.pop()
        if map.visited[cons.l_point] == 0 and map.visited[cons.r_point] == 0:
            removed, isaviliable = remove(map, cons.l_point, cons.r_point, del_index, del_color)
            if isaviliable == 0:
                flag = 0
                break
            elif removed == 1:
                for i in range(len(map.neighbour[cons.l_point])):
                    checklist.append(constraint(map.neighbour[cons.l_point][i], cons.l_point))
    return flag


def Back_AC3(map, step, s_type):
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
        if s_type == 1:
            tt = location
            for i in range(tt, len(map.states)):
                if map.visited[i] == 0 and map.num_neighbour[i] > map.num_neighbour[location]:
                    location = i
        if s_type == 2:
            tt = location
            for i in range(tt, len(map.states)):
                if map.visited[i] == 0 and len(map.datalist[i]) < len(map.datalist[location]):
                    location = i
        map.visited[location] = 1
        for i in range(len(map.datalist[location])):
            del_index = []
            del_color = []
            map.colors[location] = map.datalist[location][i]
            isaviliable = 1
            for j in range(len(map.neighbour[location])):
                if map.visited[map.neighbour[location][j]] != 0 and map.colors[map.neighbour[location][j]] == \
                        map.colors[location]:
                    isaviliable = 0
                if map.visited[map.neighbour[location][j]] == 0:
                    if map.colors[location] in map.datalist[map.neighbour[location][j]]:
                        dindex = map.datalist[map.neighbour[location][j]].index(map.colors[location])
                        map.datalist[map.neighbour[location][j]].pop(dindex)
                        if len(map.datalist[map.neighbour[location][j]]) == 0:
                            isaviliable = 0
                        del_index.append(map.neighbour[location][j])
                        del_color.append(map.colors[location])
            if AC3_check(map, del_index, del_color) == 0:
                isaviliable = 0
            if isaviliable == 1:
                Back_AC3(map, step + 1, s_type)
            for j in range(len(del_index)):
                map.datalist[del_index[j]].append(del_color[j])
        map.visited[location] = 0
        map.colors[location] = -1
    return 0
