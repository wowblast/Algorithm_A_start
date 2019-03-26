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


def initialize(G, pos, start, goal):
    # define start and goal nodes
    color_map = []
    node_size = []

    #ojo a este dato
    #G.add_nodes_from(pos.keys())
   
    
    
    for node in enumerate(G):
        # start node
        
        ''' nodonuevo = Node(node[1],list(G.edges(node[1])),"null",0)
        print nodonuevo.__str__()
        nodonuevo.define_parent("xqc")
        print ("nuevos padres son ",nodonuevo.parent)'''

        if node[1] == start:
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
    '''nx.draw_networkx(G, pos=pos, with_labels=False, node_color=color_map, node_size=node_size)
    plt.xticks(np.arange(0, 20))
    plt.yticks(np.arange(0, 20))
    plt.show()'''



# def heuristic():
#     h = "your heuristic estimate"
#     return h
def heuristich_funtion(point,point2):
    return abs(point[0] - point2[0]) + abs(point[1]-point2[0])

# def getNeighbors():
#     return "list of neighors"
def getall_possible_children(current_point,goal_point,G):
    lista_possible_ways =list()
    
    for child in current_point.children:
        lista_possible_ways.append(Node(child,list(G.edges(child)),current_point.pos,1+current_point.cost_total,(current_point.cost_total+heuristich_funtion(child,goal_point))))
        #(current_point.cost_total+heuristich_funtion(child,goal_point))
    return  lista_possible_ways 


# def searchPath(G):
#     return path


        
def algotith_a_star(startpoint,goal,G):
    print "running"
    openlist =list()
    closetlist = list()
    current = Node(startpoint,list(G.edges(startpoint)),"zero",0,heuristich_funtion(startpoint,goal))
   
    openlist.append (current)
    while openlist:
        print current.__str__()
        if current.pos == goal:
            print "llego a la posicion"
            break
        else:

            openlist.extend( getall_possible_children(current,goal,G))
        
            if openlist:

                next_point =min([child.heuristic for child in openlist])
                actual_list =list(openlist)
                
                for child in actual_list:
                    if child.heuristic == next_point:
                        current =  Node(child.pos,list(G.edges(child.pos)),current.pos,1+ current.cost_total,heuristich_funtion(child.pos,goal)) 
                    
                    openlist.append(Node(child.pos,list(G.edges(child.pos)),current.pos,1+ current.cost_total,heuristich_funtion(child.pos,goal)) )   
            else:
                break 
            
        closetlist.append(current) 

    for node in openlist:
        print "openlsit",node.__str__()   
    for node in closetlist:
        print node.__str__()      
    
    
    #While the open set is not empty
    

    #execute_heuristich_funtion()
    print "executing algotith_a_star"    

def newList(current_list):
    new_list= current_list
    return new_list

# def plotPath(G, path):
#     nx.draw("show the path within the graph")
#     print path


def main():
    G, pos = loadData()
    start_node = (2,19)
    goal_node = (10,10)
    #algotith_a_star()
    algotith_a_star(start_node,goal_node,G)

    initialize(G, pos, start_node, goal_node)
    
    ''' you have to develop the rest of the functions '''
    # searchPath()
   
    # plotPath()



# when you call the script, it will start here
if __name__ == "__main__":
    main()
