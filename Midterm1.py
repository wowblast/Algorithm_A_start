import networkx as nx
import matplotlib.pylab as plt
import numpy as np
import pickle


class Node():
    def __init__(self,pos, children, parent,cost_total,heuristic):
        
        self.pos = pos                        
        self.children=[child[1] for child in children if (child[1]!=parent and child[1][1]<=pos[1])  ]          
        self.parent = parent
        self.cost_total=cost_total
        self.heuristic=heuristic
    
    def define_parent(self,parent):
        self.parent = parent

    def __str__(self):
         return ' position: {}  childrens: {}  parents {} cost {} heuristic {}'.format(self.pos,self.children, self.parent,self.cost_total, self.heuristic)   

def loadData():
    # load graph information
    pickle_in = open("Midterm1.pickle","rb")
    data = pickle.load(pickle_in)
    return data[0], data[2]


def initialize(G, pos, start, goal,final_path):
    # define start and goal nodes
    color_map = []
    node_size = []

    
   
    
    
    for node in enumerate(G):
        # start node
        
        ''' nodonuevo = Node(node[1],list(G.edges(node[1])),"null",0)
        print nodonuevo.__str__()
        nodonuevo.define_parent("xqc")
        print ("nuevos padres son ",nodonuevo.parent)'''
        
        if (node[1] in final_path) and node[1] != start:
            color_map.append('yellow')
            node_size.append(100)
        elif node[1] == start:
            color_map.append('green')
            node_size.append(200)
        # end node
        elif node[1] == goal:
            color_map.append('blue')
            node_size.append(200)
        # all others
        
        else:
            color_map.append('red')
            node_size.append(50)
        

    # plot graph
    nx.draw_networkx(G, pos=pos, with_labels=False, node_color=color_map, node_size=node_size)
    plt.xticks(np.arange(0, 20))
    plt.yticks(np.arange(0, 20))
    plt.show()



# def heuristic():
   
def heuristic_funtion(point,point2):
    return abs(point[0] - point2[0]) + abs(point[1]-point2[0])

# def getNeighbors():
#     
def getNeighbors(current_point,goal_point,G):
    lista_possible_ways =[]
    
    for child in current_point.children:
        lista_possible_ways.append(Node(child,list(G.edges(child)),current_point.pos,1+current_point.cost_total,(heuristic_funtion(child,goal_point))))
        
    return  lista_possible_ways 


# def searchPath(G):
#     return path


        
def algorithm_a_star(startpoint,goal,G):
    #define empty list
    openlist =[]
    closetlist = []
    current = Node(startpoint,list(G.edges(startpoint)),(-8,-8),0,heuristic_funtion(startpoint,goal))
   
    openlist.append (current)
    #While the open set is not empty
    while  openlist:
        
        arrive = False
        
        if current.pos == goal:
            arrive = True
            break
        else:
            closetlist.append(current)  
            if current.children == []:
                if openlist==[]:
                    break                
                for x in range(len(openlist)-1,-1,-1):
                   
                    if openlist[x].pos == current.pos:                        
                        
                        del openlist[x]
                if openlist==[]:
                    continue       
                next_point =min([child.heuristic for child in openlist])
                                    
                for child in openlist:
                    if child.heuristic == next_point:
                        current =  child                                     
                                               
            elif openlist:                                                
                openlist.extend( getNeighbors(current,goal,G))
                for x in range(len(openlist)-1,-1,-1):
                    
                    if openlist[x].pos == current.pos:                        
                        
                        del openlist[x]
                        if openlist==[]:
                            break
                next_point =min([child.heuristic for child in openlist])
                
                for child in openlist:
                    if child.heuristic == next_point:
                        current =  child              
               
            else:
                break 
    return closetlist, arrive  
    
# set the path from initial node to the final
def path(list_path,start_goal):
    all_path =[]
    tail = list_path[len(list_path)-1].parent
    all_path.append(list_path[len(list_path)-1].pos)
    all_path.append(tail)
    while tail !=(-8,-8):
        for x in range(len(list_path)-1,-1,-1):
            if list_path[x].pos == tail:
                tail = list_path[x].parent
                if tail != (-8,-8) or tail != start_goal :
                    
                    all_path.append(tail)
                    continue
                
    return all_path

def main():
    #initial nodes
    G, pos = loadData()
    start_node = (0,18)
    goal_node = (15,0)
    
    # searchPath()
    all_path,arrive =algorithm_a_star (start_node,goal_node,G)
   
   
    final_path =[]
    if all_path  and arrive:
        final_path =path(all_path,start_node)
    elif all_path and not arrive:
        for child in all_path:
            final_path.append(child.pos)    
       
   
    # plotPath()    
    initialize(G, pos, start_node, goal_node,final_path)
       


# when you call the script, it will start here
if __name__ == "__main__":
    main()
