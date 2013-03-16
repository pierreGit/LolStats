        
class ItemInfos(dict):
    """Class storing some information about this item :
    - price ;
    - evolvability ;
    - restrictions"""
    
    def __init__(self, price, evolv, restrict):
        """Constructor"""
        self["price"] = price
        self["evolv"] = evolv
        self["restrict"] = restrict
        
    def __getattr__(self, attr):
        return self[attr]
        
class Item(dict):
    
    def __init__(self, name, carac, caracAura, passifList, actifList, infos):
        self["name"] = name
        self["bonuses"] = carac
        self["bonusesAura"] = caracAura
        self["passifs"] = passifList
        self["actifs"] = actifList
        self["infos"] = infos
    
    def __getattr__(self, attr):
        return self[attr]
    
