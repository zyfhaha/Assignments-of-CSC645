from TicAction import  TicAction

class TicState:
    def __init__(self):
        self.field=[]
        for i in range(9):
            self.field.append(0)