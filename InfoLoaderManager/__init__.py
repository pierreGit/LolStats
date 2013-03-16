from dbInterface.dbInterface import DBInterface
from htmlLoader.htmlItemLoader import loadItem, listItems
from htmlLoader.htmlChpLoader import listChmp, loadChmp
from statsManager.statsManager import StatsManager


class LoadManager:
    """Class doing all the loading job """
    
    def __init__(self):
        self.dbInterface = DBInterface()
        self.statsMngr = StatsManager()
        
    def loadItems(self):
        itemsList = listItems()
        
        for item in itemsList:
            item = loadItem("http://leagueoflegends.wikia.com" + item)
            self.dbInterface.insertItem(item)

    def testLoading(self):
        self.dbInterface.displayCollection()
        itemHealth = self.statsMngr.extractBonusValue("health", self.dbInterface.getCollection())
        sortedList = self.statsMngr.sortBonusValue("health", itemHealth)
        print sortedList
        self.statsMngr.createTable(sortedList, "goldValue")
        self.statsMngr.saveHtml()
        
    def testLoadAllChmp(self):
        l = listChmp()
        
        for c in l:
            loadChmp(c)
    
    def testLoadingItems(self):
        l = listItems()
        print l
        print len(l)
        for item in l:
            i = loadItem("http://leagueoflegends.wikia.com" + item)
            print i
            self.dbInterface.insertItem(i)
            
    def testLoadingAuraItem(self):
        item = loadItem("http://leagueoflegends.wikia.com/wiki/Aegis_of_the_Legion")
        print item
        
        
LoadManager().testLoadingAuraItem()
