import sys
import getopt
class Node():
    def __init__(self,name,pos, children, partent):
        self.name = name
        self.pos = pos
        self.children = [x[1] for x in children]
        self.partent = partent    
    
    def define_parent(self,parent):
        self.parent = parent

    def __str__(self):
         return 'name :{} position: {}  childrens: {}  parents {}'.format(self.name,self.pos,self.children, self.partent)   
