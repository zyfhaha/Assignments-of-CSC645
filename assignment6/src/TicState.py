from TicAction import TicAction

class TicState:
    def __init__(self, player):
        self.field = []
        for i in range(9):
            self.field.append(0)
        self.player = player
        self.utility = 0
        self.line=-1
        self.llist=[0,3,6,0,1,2,0,2]

    def updateUtility(self):
        if self.isTerminal()==1:
            if self.line==-1:
                self.utility=0
            else:
                self.utility=self.field[self.llist[self.line]]
        else:
            self.utility=0

    def isTerminal(self):
        t=1
        for i in range(len(self.field)):
            if self.field[i]==0:
                t=0
        if t==1:
            self.line=-1
            return 1
        if self.field[0]==self.field[1] and self.field[1]==self.field[2] and self.field[0]!=0:
            self.line=0
            return 1
        if self.field[3]==self.field[4] and self.field[4]==self.field[5] and self.field[3]!=0:
            self.line=1
            return 1
        if self.field[6]==self.field[7] and self.field[6]==self.field[8] and self.field[6]!=0:
            self.line=2
            return 1
        if self.field[0]==self.field[3] and self.field[3]==self.field[6] and self.field[0]!=0:
            self.line=3
            return 1
        if self.field[1]==self.field[4] and self.field[4]==self.field[7] and self.field[1]!=0:
            self.line=4
            return 1
        if self.field[2]==self.field[5] and self.field[5]==self.field[8] and self.field[2]!=0:
            self.line=5
            return 1
        if self.field[0]==self.field[4] and self.field[4]==self.field[8] and self.field[0]!=0:
            self.line=6
            return 1
        if self.field[2]==self.field[4] and self.field[4]==self.field[6] and self.field[2]!=0:
            self.line=7
            return 1
        return 0

    def getresult(self, action):
        new_s=TicState(self.player*(-1))
        new_s.field=list(self.field)
        new_s.field[action.position]=action.player
        new_s.updateUtility()
        return new_s

    def getActions(self):
        p=[]
        for i in range(len(self.field)):
            if self.field[i]==0:
                p.append(TicAction(self.player,i))
        return p

    def ansprint(self):
        dict = {-1: 'O', 1: '#', 0: ' '}
        print(dict[self.field[0]], '|', dict[self.field[1]], '|', dict[self.field[2]])
        print('-','+','-','+','-')
        print(dict[self.field[3]], '|', dict[self.field[4]], '|', dict[self.field[5]])
        print('-', '+', '-', '+', '-')
        print(dict[self.field[6]], '|', dict[self.field[7]], '|', dict[self.field[8]])
