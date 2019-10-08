from TicAction import TicAction


class TicState:
    def __init__(self, player):
        self.field = []
        for i in range(9):
            self.field.append(0)
        self.player = player
        self.utility = 0

    def updateUtility(self):
        self.utility = 0

    def isTerminal(self):
        return 0

    def ansprint(self):
        return None