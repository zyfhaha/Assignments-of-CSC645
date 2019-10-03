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
        self.datalist = []
        self.borders = []
        self.neighbour=[]
        self.num_neighbour=[]
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
            self.neighbour.append([])


        for k in range(9):
            combolist=[]
            for i in range(9):
                combolist.append(k*9+i)
            for i in range(len(combolist)-1):
                for j in range(i+1,len(combolist)):
                    if i!=j:
                        self.borders.append(Border(combolist[i],combolist[j]))
        for k in range(9):
            combolist=[]
            for i in range(9):
                combolist.append(k+i*9)
            for i in range(len(combolist)-1):
                for j in range(i+1,len(combolist)):
                    if i!=j:
                        self.borders.append(Border(combolist[i],combolist[j]))

        combolist=[0,1,2,9,10,11,18,19,20]
        for i in range(len(combolist) - 1):
            for j in range(i + 1, len(combolist)):
                if i != j:
                    self.borders.append(Border(combolist[i], combolist[j]))
                    self.borders.append(Border(combolist[i]+27, combolist[j]+27))
                    self.borders.append(Border(combolist[i]+54, combolist[j]+54))

        combolist=[3,4,5,12,13,14,21,22,23]
        for i in range(len(combolist) - 1):
            for j in range(i + 1, len(combolist)):
                if i != j:
                    self.borders.append(Border(combolist[i], combolist[j]))
                    self.borders.append(Border(combolist[i] + 27, combolist[j] + 27))
                    self.borders.append(Border(combolist[i] + 54, combolist[j] + 54))

        combolist=[6,7,8,15,16,17,24,25,26]
        for i in range(len(combolist) - 1):
            for j in range(i + 1, len(combolist)):
                if i != j:
                    self.borders.append(Border(combolist[i], combolist[j]))
                    self.borders.append(Border(combolist[i] + 27, combolist[j] + 27))
                    self.borders.append(Border(combolist[i] + 54, combolist[j] + 54))

        for i in range(len(self.borders)):
            self.neighbour[self.borders[i].index1].append(self.borders[i].index2)
            self.neighbour[self.borders[i].index2].append(self.borders[i].index1)

        for i in range(len(self.neighbour)):
            self.num_neighbour.append(len(self.neighbour[i]))

    def isgoal(self):
        flag = 1
        for i in range(len(self.borders)):
            if self.colors[self.borders[i].index1] == self.colors[self.borders[i].index2]:
                flag = 0
                break
        return flag

    def picprint(self):
        for i in range(9):
            for j in range(9):
                print(self.colors[i*9+j],end=' ')
            print()

    def textprint(self):
        return 0
