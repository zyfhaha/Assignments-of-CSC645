from Minimax import Minimax
from TicState import TicState

dict={(-1,'O'),(1,'#'),(0,' ')}
print('Do you want to use alpha-beta purning?(Y/N)')
ch=input()
if ch=='Y':
    minimax=Minimax(1)
else:
    minimax=Minimax(0)
print("The squares are numbered as follows:")
print("1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n")
print("Who should start? 1=you 2=computer ")
st=int(input())
if st==1:
    st=-1
    s=TicState(-1)
else:
    st=1
    s=TicState(1)

while 

