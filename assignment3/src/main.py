#! /usr/bin/env python3
import math
from Vector2D import Vector2D
from environment import Environment

class Node:
    def __init__(self,num=0,g=0,h=0):
        self.point_num=num
        self.g=g
        self.h=h
        self.pathlist=[]

def dist_h(env,num):   # To calculate h(x) of points[num]
    return math.sqrt((env.goal.x-env.points[num].x)*(env.goal.x-env.points[num].x)+(env.goal.y-env.points[num].y)*(env.goal.y-env.points[num].y))

def greedySearch(env):
    visited = []
    openlist = []
    for i in range(len(env.points)):
        visited.append(0)
    p = Node(0, 0)
    p.h = dist_h(env, 0)
    openlist.append(p)
    while visited[1] == 0:
        min_point = 0
        for i in range(len(openlist)):
            if (openlist[i].h) < (openlist[min_point].h):
                min_point = i
        search_node = openlist.pop(min_point)
        visited[search_node.point_num] = 1
        for i in range(len(env.points)):
            if (env.neighbor[search_node.point_num][i] >= 0) and (visited[i] == 0):
                new_node = Node(i, search_node.g + env.neighbor[search_node.point_num][i], dist_h(env, i))
                new_node.pathlist = list(search_node.pathlist)
                new_node.pathlist.append(env.points[search_node.point_num])
                flag = -1
                for j in range(len(openlist)):
                    if openlist[j].point_num == new_node.point_num:
                        flag = j
                if flag == -1:
                    openlist.append(new_node)
                else:
                    if new_node.h < openlist[flag].h:
                        openlist.pop(flag)
                        openlist.append(new_node)
    search_node.pathlist.append(env.points[1])
    print("The length of the path:",search_node.g+search_node.h)
    return search_node.pathlist

def uniformCostSearch(env):
    visited = []
    openlist = []
    for i in range(len(env.points)):
        visited.append(0)
    p = Node(0, 0)
    p.h = dist_h(env, 0)
    openlist.append(p)
    while visited[1] == 0:
        min_point = 0
        for i in range(len(openlist)):
            if (openlist[i].g) < (openlist[min_point].g):
                min_point = i
        search_node = openlist.pop(min_point)
        visited[search_node.point_num] = 1
        for i in range(len(env.points)):
            if (env.neighbor[search_node.point_num][i] >= 0)and(visited[i]==0):
                new_node = Node(i, search_node.g + env.neighbor[search_node.point_num][i], dist_h(env, i))
                new_node.pathlist = list(search_node.pathlist)
                new_node.pathlist.append(env.points[search_node.point_num])
                flag = -1
                for j in range(len(openlist)):
                    if openlist[j].point_num == new_node.point_num:
                        flag = j
                if flag == -1:
                    openlist.append(new_node)
                else:
                    if new_node.g  < openlist[flag].g :
                        openlist.pop(flag)
                        openlist.append(new_node)
    search_node.pathlist.append(env.points[1])
    print("The length of the path:",search_node.g + search_node.h)
    return search_node.pathlist

def astarSearch(env):
    visited=[]             #visit[i]==1 means points[i] is visited
    openlist=[]
    for i in range(len(env.points)):
        visited.append(0)
    p=Node(0,0)
    p.h=dist_h(env,0)
    openlist.append(p)
    while visited[1]==0:    #We label the goal point as points[1], if the goal point is visited, end the loop
        min_point=0
        for i in range(len(openlist)):
            if (openlist[i].g+openlist[i].h)<(openlist[min_point].g+openlist[min_point].h):
                min_point=i
        search_node=openlist.pop(min_point)
        visited[search_node.point_num]=1
        for i in range(len(env.points)):
            if (env.neighbor[search_node.point_num][i]>=0) and (visited[i]==0):
                new_node=Node(i,search_node.g+env.neighbor[search_node.point_num][i],dist_h(env,i))
                new_node.pathlist=list(search_node.pathlist)
                new_node.pathlist.append(env.points[search_node.point_num])
                flag=-1
                for j in range(len(openlist)):
                    if openlist[j].point_num==new_node.point_num:
                        flag=j
                if flag==-1:
                    openlist.append(new_node)
                else:
                    if new_node.g+new_node.h<openlist[flag].g+openlist[flag].h:
                        openlist.pop(flag)
                        openlist.append(new_node)
    search_node.pathlist.append(env.points[1])
    print("The length of the path:",search_node.g + search_node.h)
    return search_node.pathlist

if __name__ == '__main__':
    env = Environment('output/environment.txt')
    print("Loaded an environment with {} obstacles.".format(len(env.obstacles)))

    searches = {
        'greedy': greedySearch,
        'uniformcost': uniformCostSearch,
        'astar': astarSearch
    }

    for name, fun in searches.items():
        print("Attempting a search with " + name)
        Environment.printPath(name, fun(env))
