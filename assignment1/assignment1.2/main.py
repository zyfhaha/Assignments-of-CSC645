from environment import environment
from agents import agents,cleaner

print('Please input the cleanliness of the rooms(a list of number separated by space like 1 0 1 1 0 1):')
print('-------------------------number 1 means dirty, number 0 means clean-----------------------------')
arr=list(map(int,input().split()))
searchroom=environment(len(arr),arr)
robot=cleaner(0)
robot.sensor(searchroom)
robot.printroom()
ch=input()
while (ch!='q'):
    if ord(ch)>=ord('A') and ord(ch)<=ord('Z'):
        searchroom.droplitter(ord(ch)-ord('A'))
    robot.actuator(robot.decision())
    robot.printroom()
    ch=input()