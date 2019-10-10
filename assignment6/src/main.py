from Minimax import Minimax
from TicState import TicState
from TicAction import TicAction

print('Do you want to use alpha-beta purning?(Y/N)')
ch = input()
if ch == 'Y':
    minimax = Minimax(1)
else:
    minimax = Minimax(0)
print("The squares are numbered as follows:")
print("1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n")
print("Who should start? 1=you 2=computer ")
st = int(input())
if st == 1:
    st = -1
    s = TicState(-1)
    s.updateUtility()
else:
    st = 1
    s = TicState(1)
    s.updateUtility()
print('The initial state is :')
s.ansprint()
print('Your label is O, the computer is #')

while s.isTerminal() == 0:
    if st == 1:
        st = -1
        s = s.getresult(minimax.MinimaxDecision(s))
        s.player = -1
        if ch == 'Y':
            minimax = Minimax(1)
        else:
            minimax = Minimax(0)
        print('The computer set a square: ')
    else:
        st = 1
        print('Which square do you want to set? (1--9) ')
        temp = int(input())
        while temp < 1 or temp > 9 or s.field[temp - 1] != 0:
            print('You must give a valid input!!!')
            temp = int(input())
        a = TicAction(-1, temp - 1)
        s = s.getresult(a)
        s.player = 1
    s.ansprint()
if s.utility == 0:
    print('Draw')
elif s.utility == 1:
    print('You lost')
else:
    print('You win')
