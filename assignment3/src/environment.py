from polygon import Polygon
from vector2d import Vector2D
import math

def cross(p1, p2, p3):
    x1 = p2.x - p1.x
    y1 = p2.y - p1.y
    x2 = p3.x - p1.x
    y2 = p3.y - p1.y
    return x1 * y2 - x2 * y1


def IsIntersec(p1, p2, p3, p4):     #If the line segment (p1, p2) intersects with (p3, p4), return 1; otherwise, return 0.
    if (max(p1.x, p2.x) > min(p3.x, p4.x)
            and max(p3.x, p4.x) > min(p1.x, p2.x)
            and max(p1.y, p2.y) > min(p3.y, p4.y)
            and max(p3.y, p4.y) > min(p1.y, p2.y)):
        if (cross(p1, p2, p3) * cross(p1, p2, p4) < 0
                and cross(p3, p4, p1) * cross(p3, p4, p2) < 0):
            D = 1
        else:
            D = 0
    else:
        D = 0
    return D

class Environment:

    def __init__(self, filename):
        self.width = 800
        self.height = 600
        self.start = Vector2D(0, 0)
        self.goal = Vector2D(800, 600)
        self.obstacles = []
        self.points = []                  #store all of the points in the problem
        self.sides_point1 = []
        self.sides_point2 = []
        self.neighbor= []                 #a two-dimensional list if point j can not be successor point of i, neighbor[i][j]=-1, else store the distace between the two points
        self.start.polygon_num=-1
        self.goal.polygon_num=-2
        self.points.append(self.start)
        self.points.append(self.goal)

        f = open(filename, 'r')
        envtxt = f.readlines()
        f.close()
        polygonstxt, *resttxt = envtxt
        polygons = int(polygonstxt)
        for polygon_number in range(polygons):
            ntxt, *resttxt = resttxt
            n = int(ntxt)
            p = Polygon(n)
            for line in resttxt[:n]:
                [x, y] = [float(x) for x in line.split()]
                p.vertices.append(Vector2D(x, y))
            resttxt = resttxt[n:]
            self.obstacles.append(p)

        #put all of the points into self.points
        for i in range(len(self.obstacles)):
            for j in range(len(self.obstacles[i].vertices)):
                if abs(self.obstacles[i].vertices[j].x-self.obstacles[i].vertices[(j+1)%self.obstacles[i].sides].x)>0.000001 or abs(self.obstacles[i].vertices[j].y-self.obstacles[i].vertices[(j+1)%self.obstacles[i].sides].y)>0.000001 :
                    self.sides_point1.append(self.obstacles[i].vertices[j])
                    self.sides_point2.append(self.obstacles[i].vertices[(j+1)%self.obstacles[i].sides])
                point=self.obstacles[i].vertices[j]
                point.polygon_num=i
                point.point_num=j
                self.points.append(point)


        #Building a two-dimensional list self.neighbor
        for i in range(len(self.points)):
            pl=list([])
            for j in range(len(self.points)):
                dist=math.sqrt((self.points[i].x - self.points[j].x) * (self.points[i].x - self.points[j].x) + (self.points[i].y - self.points[j].y) * (self.points[i].y - self.points[j].y))
                if i==j:
                    pl.append(-1)
                else:
                    if self.points[i].polygon_num==self.points[j].polygon_num:
                        nn = self.obstacles[self.points[i].polygon_num].sides
                        if (self.points[i].point_num - self.points[j].point_num + nn) % nn ==1 or (self.points[j].point_num - self.points[i].point_num + nn) % nn ==1 :
                            pl.append(dist)
                        else:
                            pl.append(-1)
                    else:
                        flag=0
                        for k in range(len(self.sides_point1)):
                            if IsIntersec(self.points[i],self.points[j],self.sides_point1[k],self.sides_point2[k])==1:
                                flag=1
                        if flag==1:
                            pl.append(-1)
                        else:
                            pl.append(dist)
            self.neighbor.append(pl)

    @staticmethod
    def printPath(searchName, path):
        print("The nodes in the path:")
        for i in range(len(path)):
            print('[{}, {}]'.format(path[i].x, path[i].y))
        print()
        with open('output/' + searchName + '.js', 'w') as f:
            f.write('window.' + searchName + ' =\n\t[\n')
            for v in range(len(path)):
                f.write('\t\t[{}, {}],\n'.format(path[v].x, path[v].y))
            f.write('\t];\n')
