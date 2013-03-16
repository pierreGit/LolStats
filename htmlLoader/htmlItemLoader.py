from bs4 import BeautifulSoup, NavigableString
from model.sharedModel import Statistics, statLabel
from model.itemModel import Item, ItemInfos
import urllib

def loadItemName(itemBox):
    return itemBox.find("tr").td.b.string
    
def testItemInfo(line):
    info = line.find("th")
    return info.string if info else ""
  

def loadItemStats(statsLines):
    stats = Statistics()
    for child in [c for c in statsLines.children][:2]:
        if isinstance(child, NavigableString):
            print child.string.split("%")[0]
            value = int(child.string.split("%")[0])
        else:
            if child.name == "a":
                stats[statLabel(child.string.lower())] = value
                
    return stats

def loadItemInfos(infosLines, itemName):
    
    infos = ItemInfos(int(infosLines.span.string.split(" ")[0].replace('g', '')), None, None)
    
    return infos

def loadItemAura(auraLines, itemName):
    print auraLines
    print type(auraLines)
    print auraLines.string
    
    cc = [c for c in auraLines.contents]
    print cc

def loadItemPassive(passiveLines, itemName):
    pass
    #print("passive")

def loadItemActive(activeLines, itemName):
    #print("active")
    pass

def loadItem(itemPageLink):
    f = urllib.urlopen(itemPageLink)
    html = f.read()
    
    soup = BeautifulSoup(html)
    
    if len(soup.select("div#mw-content-text table.infobox")) == 0:
        return Item("", Statistics(), None, None, None, "")
    
    box = soup.select("div#mw-content-text table.infobox")[0]
    name = loadItemName(box)
    stats = Statistics()
    
    for line in box.findAll("tr"):
        resTest = testItemInfo(line)
        if resTest == "Stats":
            stats = loadItemStats(line.find("td"))
        elif resTest == "Aura":
            infos = loadItemAura(line.find("td"), name)
        elif resTest == "Passive":
            infos = loadItemPassive(line.find("td"), name)
        elif resTest == "Active":
            infos = loadItemActive(line.find("td"), name)
        elif resTest == "Item cost":
            infos = loadItemInfos(line.find("td"), name)
    
    item = Item(name, stats, None, None, None, infos)
    return item
        
def listItems():
    searchurl = "http://leagueoflegends.wikia.com/wiki/Item"
    f = urllib.urlopen(searchurl)
    html = f.read()
    
    soup = BeautifulSoup(html)
    
    div = soup.find("div", class_="va-collapsible-content mw-collapsible-content")
    tables = [child for child in div.children if (not isinstance(child, NavigableString))][:5]
    itemLinks = []
    
    for t in tables:
        itemsLines = [tr.find("td") for tr in t.findAll("tr")[1:]]
        
        for itemsline in itemsLines:
            itemLinks.append([itemLink["href"] for itemLink in itemsline.findAll("a")])

    itemLinks = [item for sublist in itemLinks for item in sublist]
    return itemLinks