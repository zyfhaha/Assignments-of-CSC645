class Border:
    def __init__(self, in1, in2):
        self.index1 = in1
        self.index2 = in2


class Sudoku:
    def __init__(self):
        line1 = [0, 0, 3, 0, 2, 0, 6, 0, 0]
        line2 = [9, 0, 0, 3, 0, 5, 0, 0, 1]
        line3 = [0, 0, 1, 8, 0, 6, 4, 0, 0]
        line4 = [0, 0, 8, 1, 0, 2, 9, 0, 0]
        line5 = [7, 0, 0, 0, 0, 0, 0, 0, 8]
        line6 = [0, 0, 6, 7, 0, 8, 2, 0, 0]
        line7 = [0, 0, 2, 6, 0, 9, 5, 0, 0]
        line8 = [8, 0, 0, 2, 0, 3, 0, 0, 9]
        line9 = [0, 0, 5, 0, 1, 0, 3, 0, 0]
        self.states = []
        self.colors = []
        self.visited = []
        self.datalist=[]
        self.colors.extend(line1)
        self.colors.extend(line2)
        self.colors.extend(line3)
        self.colors.extend(line4)
        self.colors.extend(line5)
        self.colors.extend(line6)
        self.colors.extend(line7)
        self.colors.extend(line8)
        self.colors.extend(line9)
        for i in range(len(self.colors)):
            self.states.append(i)
            if self.colors[i] != 0:
                self.visited.append(1)
            else:
                self.visited.append(0)
            self.datalist.append([1,2,3,4,5,6,7,8,9])
