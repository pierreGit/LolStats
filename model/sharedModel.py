'''
Created on 24 janv. 2013

@author: pierre
'''

class Statistics(dict):
    """Class listing all standard attributes :
    - name ;
    - price ;
    - bonuses ;
    - effects"""

    def __init__(self):
        pass
    
    def __getattr__(self, attr):
        return self[attr]
    
    def __setattr__(self, attr, value):
        self[attr] = value
  
    def hasAttr(self, attr):
        return self.has_key(attr)
  
    def setInitialValues(self):
        self["health"] = 0
        self["mana"] = 0
        self["healthRgn"] = 0
        self["manaRgn"] = 0
        self["attackDmg"] = 0
        self["attackSpd"] = 0
        self["criticalStkChc"] = 0
        self["abilityPwr"] = 0
        self["cooldownRdt"] = 0
        self["armor"] = 0
        self["magicRst"] = 0
        self["mouvementSpd"] = 0
        self["lifeStl"] = 0
        self["spellVp"] = 0
        self["magicPen"] = 0
        self["armorPen"] = 0
        
def statLabel(x):
    return {
        'health': "health",
        'attack damage': "attackDmg",
        'ability power': "abilityPwr",
        'attack speed': "attackSpd",
        'armor penetration': "armorPen",
        'life steal': "lifeStl",
        'armor': "armor",
        'mana': "mana",
        'movement speed': "movementSpd",
        'magic resistance': "magicRst",
        'magic penetration': "magicPen",
        'critical strike chance': "criticalStkChc", 
        'mana regeneration': "manaRgn",
        'health regeneration': "healthRgn",
        'mana regen': "manaRgn",
        'health regen': "healthRgn",
        'armor': "armor",
        'range': "range",
        'cooldown reduction': "cooldownRdt",
        'energy': "energy",
        'energy regen.': "energyRgn",
        'heat': "heat",
        'fury': "fury",
        'ferocity': "ferocity",
    }[x]