import random
import networkx as nx
import matplotlib.pyplot as plt
from Map import Map


class Individual:
    def __init__(self, map):
        self.map = map
        self.fitness = 0
        self.colors = []
        for i in range(len(self.map.states)):
            self.colors.append(0)

    def updatefitness(self):
        same_num = 0
        for i in range(len(self.map.borders)):
            if self.colors[self.map.borders[i].index1] == self.colors[self.map.borders[i].index2]:
                same_num += 1
        self.fitness = 1 / (1 + same_num)
        return 0

    def isgoal(self):
        if self.fitness == 1:
            return 1
        else:
            return 0

    def mutate(self):
        ran_index = random.randint(0, len(self.map.states) - 1)
        ran_color = random.randint(1, 3)
        self.colors[ran_index] = (self.colors[ran_index] + ran_color) % 4

    def picprint(self):
        labels = {}
        for i in range(len(self.map.states)):
            labels[i + 1] = self.map.states[i]

        G = nx.Graph()
        for i in range(len(self.map.borders)):
            G.add_edge(int(self.map.borders[i].index1) + 1, int(self.map.borders[i].index2) + 1)
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
        for i in range(len(self.map.graphnum)):
            print(self.map.states[i],'(',self.colors[i],')','-->',end='')
            for j in range(len(self.map.graphnum[i])):
                print(self.map.states[self.map.graphnum[i][j]],'(',self.colors[self.map.graphnum[i][j]],')',' ',end='')
            print()
