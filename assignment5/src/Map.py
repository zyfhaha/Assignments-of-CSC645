class Border:
    def __init__(self,in1,in2):
        self.index1=in1
        self.index2=in2

class Map:
    def __init__(self,file):
        self.states=[]
        self.borders=[]
        self.graph=[]
        self.graphnum=[]
        with open(file, 'r') as f:
            for line in f:
                p = list(line.split(','))
                fin=p.pop()
                fin=fin.split('\n')
                p.append(fin[0])
                self.states.append(p[0])
                self.graph.append(p)
        for i in range(len(self.graph)):
            q=[]
            for j in range(1,len(self.graph[i])):
                for k in range(len(self.states)):
                    if self.states[k]==self.graph[i][j]:
                        self.borders.append(Border(i,k))
                        q.append(k)
            self.graphnum.append(q)