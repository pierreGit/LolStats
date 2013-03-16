'''
Created on 16 mars 2013

@author: pierre
'''

class StatsManager(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.beforeTable ='<!DOCTYPE html> <html>   <head>     <title>Bootstrap 101 Template</title>     <meta name="viewport" content="width=device-width, initial-scale=1.0">     <!-- Bootstrap -->     <link href="css/bootstrap.css" rel="stylesheet" media="screen"> <link href="css/bootstrap-responsive.min.css" rel="stylesheet" media="screen"> <style type="text/css">   #stat_table div.progress { margin-bottom: 0 } body { position: relative; padding-top: 40px }  .well .icon-chevron-right {     float: right;     margin-right: -6px;     margin-top: 2px;     opacity: 0.25; }  .affix { position: fixed;     top: 40px; }  .nav-list.well {     width: 100px; }  </style>   </head>   <body data-spy="scroll" data-target=".nav-list">               <div class="navbar navbar-inverse navbar-fixed-top">               <div class="navbar-inner">                 <div class="container" style="width: auto; padding: 0 20px;">                   <a class="brand" href="#">Title</a>                   <ul class="nav">                     <li class="active"><a href="#">Home</a></li>                     <li><a href="#">Link</a></li>                     <li><a href="#">Link</a></li>                   </ul>                 </div>               </div>             </div>  <br/> <div class="container">     <div class="row">       <div class="span2 side-nav-list">         <ul id="side-navbar" class="nav nav-list well">           <li><a href="#global"><i class="icon-chevron-right"></i> Chp1</a></li>           <li><a href="#gridSystem"><i class="icon-chevron-right"></i> Chp2</a></li>           <li><a href="#fluidGridSystem"><i class="icon-chevron-right"></i> Chp3</a></li>         </ul>       </div>       <div class="span10">      <h1>Hello, world!</h1>     <table id=stat_table class="table table-condensed table-hover">               <thead>                 <tr>                   <th>#</th>                   <th>Name</th>                   <th >Bar</th>                   <th>Stat</th>                 </tr>               </thead>               <tbody> '
        self.afterTable = '</tbody>             </table>      </div> </div>     <script src="http://code.jquery.com/jquery.js"></script>     <script src="js/bootstrap.min.js"></script>  <script> $(\'#side-navbar\').affix(); </script>    </body> </html>'
        
    def saveHtml(self):

        logfile = open('/home/pierre/Bureau/indexDB.html', 'w')
                
        logfile.write(self.beforeTable)
        logfile.write(self.table)
        logfile.write(self.afterTable)
        logfile.close()   

    def extractBonusValue(self, bonusName, itemList):
        print len(itemList)
        r=[{"name": i["name"], "price": i["infos"]["price"], bonusName:i["bonuses"][bonusName]} for i in itemList if i["bonuses"].has_key(bonusName)]
        return r
        
    def sortBonusValue(self, bonusName, itemList):
        tmp = [{"name": i["name"], "goldValue": float(i["price"])/float(i[bonusName])} for i in itemList]
        return sorted(tmp, key=lambda gv: gv["goldValue"])
    
    def createTable(self, sortedlist, sortName):
        listRange = sortedlist[-1][sortName] - sortedlist[0][sortName]
        
        self.table=""
        i = 0

        for elm in sortedlist:
            prctg = int((elm[sortName] - sortedlist[0][sortName]) / listRange * 100)
            i += 1
            self.table += "<tr> <td>" + str(i) + "</td>"
            self.table += "<td>" + elm["name"] + "</td>"
            self.table += '<td><div class="progress">'
            self.table += '<div class="bar" style="width: ' + str(100 - prctg) + '%;"></div></div></td>'
            self.table += '<td>' + str(elm[sortName])[0:4] + '</td></tr>'
            