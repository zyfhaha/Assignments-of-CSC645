import networkx as nx
import matplotlib.pyplot as plt

class Border:
    def __init__(self, in1, in2):
        self.index1 = in1
        self.index2 = in2


class Map:
    def __init__(self, file):
        self.states = []
        self.borders = []
        self.graph = []
        self.graphnum = []
        self.visited = []
        self.datalist = []
        self.colors = []
        self.neighbour = []
        self.num_neighbour=[]
        with open(file, 'r') as f:
            for line in f:
                p = list(line.split(','))
                fin = p.pop()
                fin = fin.split('\n')
                p.append(fin[0])
                self.states.append(p[0])
                self.visited.append(0)
                self.datalist.append([0, 1, 2, 3])
                self.colors.append(-1)
                self.neighbour.append([])
                self.graph.append(p)
        for i in range(len(self.graph)):
            q = []
            for j in range(1, len(self.graph[i])):
                for k in range(len(self.states)):
                    if self.states[k] == self.graph[i][j]:
                        self.borders.append(Border(i, k))
                        q.append(k)
            self.graphnum.append(q)

        for i in range(len(self.borders)):
            self.neighbour[self.borders[i].index1].append(self.borders[i].index2)
            self.neighbour[self.borders[i].index2].append(self.borders[i].index1)

        for i in range(len(self.neighbour)):
            self.num_neighbour.append(len(self.neighbour[i]))

    def picprint(self):
        labels = {}
        for i in range(len(self.states)):
            labels[i + 1] = self.states[i]

        G = nx.Graph()
        for i in range(len(self.borders)):
            G.add_edge(int(self.borders[i].index1) + 1, int(self.borders[i].index2) + 1)
        pos = nx.spring_layout(G)
        colors = []
        nodesp = list(G.node())
        for i in range(len(nodesp)):
            ppp = self.colors[nodesp[i] - 1]
            colors.append(ppp)
        nx.draw_networkx_nodes(G, pos, node_color=colors)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, labels)
        plt.axis('off')
        plt.savefig("us_states.png")
        plt.show()

    def textprint(self):
        for i in range(len(self.graphnum)):
            print(self.states[i],'(',self.colors[i],')','-->',end='')
            for j in range(len(self.graphnum[i])):
                print(self.states[self.graphnum[i][j]],'(',self.colors[self.graphnum[i][j]],')',' ',end='')
            print()

    def isgoal(self):
        flag = 1
        for i in range(len(self.borders)):
            if self.colors[self.borders[i].index1] == self.colors[self.borders[i].index2]:
                flag = 0
                break
        return flag


