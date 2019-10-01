def Back_tracking(map,step):
    if step==len(map.states):
        if map.isgoal() == 1:
            map.picprint()
            exit()
        else:
            return 0
    
    return 0