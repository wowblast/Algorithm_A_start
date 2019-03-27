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

    #ojo a este dato
    #G.add_nodes_from(pos.keys())
   
    
    
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
#     h = "your heuristic estimate"
#     return h
def heuristich_funtion(point,point2):
    return 1+abs(point[0] - point2[0]) + abs(point[1]-point2[0])

# def getNeighbors():
#     return "list of neighors"
def getall_possible_children(current_point,goal_point,G):
    lista_possible_ways =[]
    
    for child in current_point.children:
        lista_possible_ways.append(Node(child,list(G.edges(child)),current_point.pos,1+current_point.cost_total,(heuristich_funtion(child,goal_point))))
        #(current_point.cost_total+heuristich_funtion(child,goal_point))
    return  lista_possible_ways 


# def searchPath(G):
#     return path


        
def algotith_a_star(startpoint,goal,G):
    print "running"
    openlist =[]
    closetlist = []
    current = Node(startpoint,list(G.edges(startpoint)),(-8,-8),0,heuristich_funtion(startpoint,goal))
   
    openlist.append (current)
    while  openlist:
        #print len(openlist)
        print current.__str__()
        if current.pos == goal:
            
            break
        else:
            closetlist.append(current)  
            if current.children == []:
                
                for x in range(len(openlist)):                    
                    
                    if openlist[x].pos ==current.pos:   
                        
                        del openlist[x]
                next_point =min([child.heuristic for child in openlist])
                                    
                for child in openlist:
                    if child.heuristic == next_point:
                        current =  child
                       
                                        
             
                            
                            
            elif openlist:
                
                
                        
                openlist.extend( getall_possible_children(current,goal,G))
                for x in range(0,len(openlist)-1):
                    #print openlist[x].pos , current.pos
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
            
        

    for node in openlist:
        print "openlist",node.__str__()   
    for node in closetlist:
        print node.__str__()
    return closetlist          
    
    
    #While the open set is not empty
    

    #execute_heuristich_funtion()
    

def path(list_path,start_goal):
    all_path =[]
    tail = list_path[len(list_path)-1].parent
    all_path.append(list_path[len(list_path)-1].pos)
    all_path.append(tail)
    while tail !=(-8,-8):
        for child in list_path:
            if child.pos == tail:
                tail = child.parent
                if tail != (-8,-8) or tail != start_goal:
                    all_path.append(tail)
                
    return all_path

# def plotPath(G, path):
#     nx.draw("show the path within the graph")
#     print path


def main():
    G, pos = loadData()
    start_node = (2,19)
    goal_node = (10,10)
    #algotith_a_star()
    all_path =algotith_a_star(start_node,goal_node,G)
    #current = Node(start_node,list(G.edges(start_node)),(-8,-8),0,heuristich_funtion(start_node,goal_node))
    final_path =path(all_path,start_node)
    for x in range(len(final_path)-2) :
        print final_path[x]
    initialize(G, pos, start_node, goal_node,final_path)
    '''lista = getall_possible_children(current,goal_node,G)
    for child in lista:
        print child.__str__()
    you have to develop the rest of the functions '''
    # searchPath()
   
    # plotPath()



# when you call the script, it will start here
if __name__ == "__main__":
    main()
