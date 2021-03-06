from __future__ import absolute_import

import numpy
from .Constants import Load as constLoad
from .Constants import Save as constSave

class LasingOffReference(object):
    def __init__(self):
        self.averagedProfiles=[]
        self.runs=numpy.array([],dtype=int)
        self.n=0
        self.parameters=0
        
    def Save(self,path):        
        constSave(self,path)

    @staticmethod    
    def Load(path):        
        return constLoad(path)
