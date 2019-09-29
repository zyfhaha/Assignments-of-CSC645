from environment import environment

class agents():
    def __init__(self,position=0):
        self.position=position
    def sensor(self):
        return 0
    def actuator(self):
        return 0
pass

class cleaner(agents):
    def __init__(self,position=0,):
        agents.__init__(self,position)
        self.flag=0
        self.step=0
        self.score=0
    def sensor(self,rooms):
        self.search_rooms=rooms
        if self.position==len(self.search_rooms.cleanliness)-1:
            flag=1
    def actuator(self,signal):
        if signal==0:
            print("Suck dust in the room ",chr(ord('A')+self.position))
            self.search_rooms.cleanliness[self.position]=0
            self.step+=1
            self.score+=2
        elif signal==1:
            print("Move right to the next room")
            self.position+=1
            self.step+=1
            self.score-=1
            if self.position==len(self.search_rooms.cleanliness)-1:
                self.flag=1
        elif signal==2:
            print("Move left to the next room")
            self.position -= 1
            self.step += 1
            self.score -= 1
            if self.position==0:
                self.flag=0
        else:
            print('signal error!')
    def decision(self):
        if self.search_rooms.cleanliness[self.position]==1:
            return 0
        else:
            if self.flag==0:
                return 1
            else:
                return 2
    def printroom(self):
        print('The rooms are(@ means robot, # means dirty):')
        for i in range(0,len(self.search_rooms.cleanliness)):
            print(chr(ord('A')+i),end=' ')
        print('')
        for i in range(0, len(self.search_rooms.cleanliness)):
            if i==self.position:
                print('@',end=' ')
            else:
                print(' ',end=' ')
        print('')
        for i in range(0, len(self.search_rooms.cleanliness)):
            if self.search_rooms.cleanliness[i]==1:
                print('#',end=' ')
            else:
                print(' ',end=' ')
        print('')
        if self.step!=0:
            print('Srep:',self.step,'   Score:',self.score,'  Avg_Score:',self.score/self.step)
        print('---------Input any key to continue, Input q to quit--------------')
        print('----------Input A~Z to drop litter in the room A~Z---------------')
    pass