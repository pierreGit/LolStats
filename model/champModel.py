'''
Created on 24 janv. 2013

@author: pierre
'''

class Champion(dict):
    '''
    Class representing a hero with all his caracteristics and abilities
    '''


    def __init__(self, name, stats, stats18, passive, abilities):
        self["name"] = name
        self["statistics"] = stats
        self["statistics18"] = stats18
        self["passive"] = passive
        self["abilities"] = abilities
    
    def __getattr__(self, attr):
        return self[attr]
    
      
        