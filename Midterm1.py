import networkx as nx
import matplotlib.pylab as plt
import numpy as np
import pickle


def loadData():
    # load graph information
    pickle_in = open("Midterm1.pickle","rb")
    data = pickle.load(pickle_in)
    return data[0], data[2]


def initialize(G, pos, start, goal):
    # define start and goal nodes
    color_map = []
    node_size = []
    #.add_nodes_from(pos.keys())
    #for n, p in pos.iteritems():
     #   G.node[n]['pos'] = p
    
    
    for node in enumerate(G):
        # start node
        lista = list(G.edges(node))
        print ( node[0],"  " ,node[1]," : " ,lista[0] )
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
    nx.draw_networkx(G, pos=pos, with_labels=False, node_color=color_map, node_size=node_size)
    plt.xticks(np.arange(0, 20))
    plt.yticks(np.arange(0, 20))
    plt.show()



# def heuristic():
#     h = "your heuristic estimate"
#     return h


# def getNeighbors():
#     return "list of neighors"


# def searchPath(G):
#     return path


# def plotPath(G, path):
#     nx.draw("show the path within the graph")
#     print path


def main():
    G, pos = loadData()
    start_node = (2,19)
    goal_node = (10,10)
    initialize(G, pos, start_node, goal_node)

    ''' you have to develop the rest of the functions '''
    # searchPath()

    # plotPath()



# when you call the script, it will start here
if __name__ == "__main__":
    main()
