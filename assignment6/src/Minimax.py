from TicAction import TicAction
from TicState import TicState

class Minimax:
    def __init__(self,usepurning):
        self.usepurning=usepurning
        self.numberOfStates=0

    def MinimaxDecision(self,state):
        a_list=state.getActions()
        max_act=a_list[0]
        max_ut=self.MinValue(state.getresult(a_list[0]),-2,2)
        for act in a_list:
            ut=self.MinValue(state.getresult(act),-2,2)
            if ut>max_ut:
                max_ut=ut
                max_act=act
        print('State space size: ',self.numberOfStates)
        return max_act

    def MaxValue(self,state,alpha,beta):
        self.numberOfStates+=1
        if state.isTerminal()==1:
            return state.utility
        v=-2
        a_list=state.getActions()
        for act in a_list:
            v=max(v,self.MinValue(state.getresult(act),alpha,beta))
            if self.usepurning==1:
                if v>=beta:
                    return v
                alpha=max(alpha,v)
        return v

    def MinValue(self,state,alpha,beta):
        self.numberOfStates += 1
        if state.isTerminal() == 1:
            return state.utility
        v = 2
        a_list = state.getActions()
        for act in a_list:
            v = min(v, self.MaxValue(state.getresult(act), alpha, beta))
            if self.usepurning == 1:
                if v <= alpha:
                    return v
                beta = min(beta, v)
        return v
