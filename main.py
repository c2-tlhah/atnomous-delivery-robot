import networkx as nx
import matplotlib.pyplot as plt
import random
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import matplotlib.patches as mpatches
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
ite=0
algo_used=0
maze = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

def generate_obstacles( obstacle_probability=0.2):
    for i in range(15):
        for j in range(15):
            if random.random() < obstacle_probability:
                maze[i][j] = 1

def set_obstacles():
     for i in  range(15):
          for j in range(15):
               if maze[i][j]==1:
                    obs.append((i,j))
          
curr_posi=[0,0]
x1 = 1
x2 =2
y1 =3
y2 = 4
G = nx.grid_2d_graph(15, 15)
pos = {(x, y): (y, -x) for x, y in G.nodes()} 
lis=[]
obs=[]
def manathanhuristic(start,goal):
    return abs(start[0]-goal[0])+abs(start[1]-goal[1])

def Bestfirst(start, goal, maze):
    weights = {'start': 0, 'left': 1, 'up': 2, 'down': 3, 'right': 4}
    positions = [(0, 1), (0, -1), (+1, 0), (-1, 0)]
    moves = ['right', 'left', 'down', 'up']
    c_h = manathanhuristic(start,goal)
    queue = [(start[0], start[1], ['start'], c_h)]
    visited = []
    timecomplexity = 1
    spacecomplexity = 1
    while len(queue) > 0:
        queue = sorted(queue, key=lambda tup: tup[-1])
        spacecomplexity = max(spacecomplexity, len(queue))
        if (queue[0][0], queue[0][1]) not in visited:
            c_x = int(queue[0][0])
            c_y = int(queue[0][1])
            path = []
            path = queue[0][2].copy()
            queue.pop(0)
            timecomplexity += 1
            visited.append((c_x, c_y))
            if (c_x, c_y) == goal:
                return path, timecomplexity, spacecomplexity
            if c_y + 1 < len(maze[0]) and (maze[c_x][(c_y + 1)] == 0 or maze[c_x][(c_y + 1)] == 2):
                if (c_x, c_y + 1) not in visited:
                    temp = path + ['right']
                    c_h = manathanhuristic((c_x, c_y + 1), goal)
                    queue.append((c_x, c_y + 1, temp, c_h))
            if c_y - 1 >= 0 and (maze[c_x][(c_y - 1)] == 0 or maze[c_x][(c_y - 1)] == 2):
                if (c_x, c_y - 1) not in visited:
                    temp = path + ['left']
                    c_h = manathanhuristic((c_x, c_y - 1), goal)
                    queue.append((c_x, c_y - 1, temp, c_h))

            if c_x + 1 < len(maze) and (maze[(c_x + 1)][c_y] == 0 or maze[(c_x + 1)][c_y] == 2):
                if (c_x + 1, c_y) not in visited:
                    temp = path + ['down']
                    c_h = manathanhuristic((c_x + 1, c_y), goal)
                    queue.append((c_x + 1, c_y, temp, c_h))
            if c_x - 1 >= 0 and (maze[c_x - 1][c_y] == 0 or maze[c_x - 1][c_y] == 2):
                if (c_x - 1, c_y) not in visited:
                    temp = path + ['up']
                    c_h = manathanhuristic((c_x - 1, c_y), goal)
                    queue.append((c_x - 1, c_y, temp, c_h))
        else:
            queue.pop(0)
    return [], timecomplexity, spacecomplexity

def A_star(start, goal, maze):
    weights = {'start': 0, 'left': 1, 'up': 2, 'down': 3, 'right': 4}
    maze[start[0]][start[1]]=1
    maze[goal[0]][goal[1]]=2
    positions = [(0, 1), (0, -1), (+1, 0), (-1, 0)]
    moves = ['right', 'left', 'down', 'up']
    c_h = manathanhuristic(start, goal)
    queue = [(start[0], start[1], ['start'], c_h)]
    visited = []
    timecomplexity = 1
    spacecomplexity = 1
    while len(queue) > 0:
        queue = sorted(queue, key=lambda tup: tup[-1])
        spacecomplexity = max(spacecomplexity, len(queue))
        if (queue[0][0], queue[0][1]) not in visited:
            c_x = int(queue[0][0])
            c_y = int(queue[0][1])
            path = []
            path = queue[0][2].copy()
            queue.pop(0)
            timecomplexity += 1
            visited.append((c_x, c_y))
            
            if (c_x, c_y) == goal:
                return path, timecomplexity, spacecomplexity
            if c_y + 1 < len(maze[0]) and (maze[c_x][(c_y + 1)] == 0 or maze[c_x][(c_y + 1)] == 2):
                if (c_x, c_y + 1) not in visited:
                    temp = path + ['right']
                    c_h = manathanhuristic((c_x, c_y + 1), goal)
                    sum_w = sum(weights[i] for i in temp)
                    c_h += sum_w
                    queue.append((c_x, c_y + 1, temp, c_h))
                 
            if c_y - 1 >= 0 and (maze[c_x][(c_y - 1)] == 0 or maze[c_x][(c_y - 1)] == 2):
                if (c_x, c_y - 1) not in visited:
                    temp = path + ['left']
                    c_h = manathanhuristic((c_x, c_y - 1), goal)
                    sum_w = sum(weights[i] for i in temp)
                    c_h += sum_w
                    queue.append((c_x, c_y - 1, temp, c_h))
                 
            if c_x + 1 < len(maze) and (maze[(c_x + 1)][c_y] == 0 or maze[(c_x + 1)][c_y] == 2):
                if (c_x + 1, c_y) not in visited:
                    temp = path + ['down']
                    c_h = manathanhuristic((c_x + 1, c_y), goal)
                    sum_w = sum(weights[i] for i in temp)
                    c_h += sum_w
                    queue.append((c_x + 1, c_y, temp, c_h))
                   
            if c_x - 1 >= 0 and (maze[c_x - 1][c_y] == 0 or maze[c_x - 1][c_y] == 2):
                if (c_x - 1, c_y) not in visited:
                    temp = path + ['up']
                    c_h = manathanhuristic((c_x - 1, c_y), goal)
                    sum_w = sum(weights[i] for i in temp)
                    c_h += sum_w
                    queue.append((c_x - 1, c_y, temp, c_h))
                 
        else:
            queue.pop(0)
    print(visited)
    return [], timecomplexity, spacecomplexity,visited

def algo(maze,a,b):
    global algo_used
    path_a_star, time_a_star, space_a_star = A_star(a, b, maze)
    path_best_first, time_best_first, space_best_first = Bestfirst(a, b, maze)
    print(len(path_a_star))
    print(len(path_best_first))
    # If the path found by A_star is shorter
    if len(path_a_star) < len(path_best_first):
        algo_used = 1
        return path_a_star, time_a_star, space_a_star
    # If the path found by BestFirst is shorter or the lengths are equal
    else:
        algo_used = 2   
        return path_best_first, time_best_first, space_best_first


def calc_dist(x1,y1,x2,y2):
        curr_posi[0]=x1
        curr_posi[1]=y1
        
        path,time,space = algo(maze,(x1, y1),(x2, y2))
        print(path)
        lis.append((curr_posi[0],curr_posi[1]))
        print(curr_posi)
        print(len(path))
        for i in path:
                if i == "right":
                       curr_posi[1]+=1
                       lis.append((curr_posi[0],curr_posi[1]))
                       print(curr_posi)
                elif i == "left":
                        curr_posi[1]-=1
                        lis.append((curr_posi[0],curr_posi[1]))
                        print(curr_posi) 
                if i == "down":
                        curr_posi[0]+=1
                        lis.append((curr_posi[0],curr_posi[1]))
                        print(curr_posi)
                elif i == "up":
                        curr_posi[0]-=1
                        lis.append((curr_posi[0],curr_posi[1]))  
                        print(curr_posi)
                
        print(lis)
        for i in range(15):
                print(maze[i])

def clear_up():
     global lis,x1,x2,y1,y2
     lis = []
     print("lis emptied")
     print(lis)
    

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.bg_frame = QtWidgets.QFrame(Dialog)
        self.bg_frame.setGeometry(QtCore.QRect(-1, -1, 641, 481))
        self.bg_frame.setStyleSheet("background-color: white\n")
        self.bg_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bg_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bg_frame.setObjectName("bg_frame")
        self.Graph_frame = QtWidgets.QFrame(self.bg_frame)
        self.Graph_frame.setGeometry(QtCore.QRect(19, 19, 350, 350))
        self.Graph_frame.setStyleSheet("background-color: green;\n"
                                        "border-radius:25px;")
        self.Graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Graph_frame.setObjectName("Graph_frame")
        self.deliver_button = QtWidgets.QPushButton(self.bg_frame)
        self.deliver_button.setGeometry(QtCore.QRect(400, 180, 75, 31))
        self.deliver_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-radius:10px;")
        self.deliver_button.setObjectName("deliver_button")
        self.start_input = QtWidgets.QLineEdit(self.bg_frame)
        self.start_input.setGeometry(QtCore.QRect(400, 80, 91, 20))
        self.start_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius:10px;")
        self.start_input.setObjectName("start_input")
        self.delivery_input = QtWidgets.QLineEdit(self.bg_frame)
        self.delivery_input.setGeometry(QtCore.QRect(400, 130, 91, 20))
        self.delivery_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-radius:10px;")
        self.delivery_input.setObjectName("delivery_input")
        self.label = QtWidgets.QLabel(self.bg_frame)
        self.label.setGeometry(QtCore.QRect(410, 60, 25, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.bg_frame)
        self.label_2.setGeometry(QtCore.QRect(410, 110, 81, 16))
        self.label_2.setObjectName("label_2")
        self.Displ_progress = QtWidgets.QFrame(self.bg_frame)
        self.Displ_progress.setGeometry(QtCore.QRect(410, 260, 120, 80))
        self.Displ_progress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Displ_progress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Displ_progress.setObjectName("Displ_progress")
        self.start_input.setGeometry(QtCore.QRect(400, 80, 13, 13))
        self.delivery_input.setGeometry(QtCore.QRect(400, 130, 13, 13))
        self.ite_label = QtWidgets.QLabel(self.Displ_progress)
        self.ite_label.setGeometry(QtCore.QRect(10, 10, 200, 50)) 
        self.ite_label.setObjectName("ite_label")
        self.y1_input = QtWidgets.QLineEdit(self.bg_frame)
        self.y1_input.setGeometry(QtCore.QRect(430, 80, 13, 13))
        self.y1_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius:10px;")
        self.y1_input.setObjectName("y1_input")

        self.y2_input = QtWidgets.QLineEdit(self.bg_frame)
        self.y2_input.setGeometry(QtCore.QRect(430, 130, 13, 13))
        self.y2_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "border-radius:10px;")
        self.y2_input.setObjectName("y2_input")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.deliver_button.clicked.connect(self.on_deliver_button_clicked)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.deliver_button.setText(_translate("Dialog", "Deliver"))
        self.label.setText(_translate("Dialog", "Start"))
        self.label_2.setText(_translate("Dialog", "Delivery Point"))
    def new_disp(self,x1,y1,x2,y2):
        self.canvas.figure.clear()
        node_colors = ['red' if node == (int(x1), int(y1)) or node == (int(x2), int(y2)) else 'green' if node in lis else "yellow" if node in obs else 'grey' for node in G.nodes()]
        nx.draw(G, pos, node_size=10, node_color=node_colors, with_labels=False, ax=self.figure.add_subplot(111))
        self.canvas.draw()
        
    def disp(self):
        
        self.figure = plt.figure()
        node_colors = [ "yellow" if node in obs else 'grey' for node  in G.nodes()]
        nx.draw(G, pos, node_size=10, node_color=node_colors, with_labels=False, ax=self.figure.add_subplot(111))
        self.canvas = FigureCanvas(self.figure)
        if not self.Graph_frame.layout():
                self.Graph_frame.setLayout(QtWidgets.QVBoxLayout())
        self.Graph_frame.layout().addWidget(self.canvas)

    def on_deliver_button_clicked(self):
       
        global ite,x1,y1
        if ite < 5:
            if ite==0:
                x1 = int(self.start_input.text())
                y1 = int(self.y1_input.text())
            x2 = int(self.delivery_input.text())
            y2 = int(self.y2_input.text())

          
            if not (0 <= x1 <= 14 and 0 <= y1 <= 14 and 0 <= x2 <= 14 and 0 <= y2 <= 14):
                print("Error: All values should be between 0 and 14.")
                return

        
            if (x1, y1) in obs or (x2, y2) in obs:
                print("Error: The coordinates should not be in the obstacle list.")
                return

            print("Start Point x:", x1)
            print("Delivery Point y:", x2)
            print("Start Point y:", y1)
            print("Delivery Point y:", y2)
            self.start_input.clear()
            self.delivery_input.clear()
            self.y1_input.clear()
            self.y2_input.clear()
            calc_dist(x1,y1,x2,y2)
            self.new_disp(x1,y1,x2,y2)
            clear_up()

            x1=x2
            y1=y2
        if ite < 5:    
            if algo_used == 1:
                print("Algorithm used: A*")  
                self.ite_label.setText( "Items left: " + str(4-ite)+ "\nAlgorithm used: A*")
            else:
                print("Algorithm used: Best First")
                self.ite_label.setText("Items left: " + str(4-ite)+ "\nAlgorithm used: Best First")
        else:
             self.ite_label.setText("All items delivered")

        ite+=1


if __name__ == "__main__":
    generate_obstacles()
    set_obstacles()
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.disp()
    Dialog.show()
    

    sys.exit(app.exec_())
