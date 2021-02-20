import requests
import datetime
from parsel import Selector

#url = "http://192.168.178.36/bilder/rss.1"
#urlText = requests.get(url).text
xmlFile = open("rss.xml", "r").read()
sel = Selector(text=xmlFile)

titles = sel.xpath('//item/title/text()').getall()
descriptions = sel.xpath('//item/description/text()').getall()
guidList = sel.xpath('//item/guid/text()').getall()

rssOpen = "<item>"
rssLink = "<link>animeheaven.site</link>"
#rssGuid = "<guid>animeheaven.site</guid>"
rssDate = "<pubDate>" + datetime.datetime.now().strftime("%y-%m-%d %H:%M") + "</pubDate>"
rssClose = "</item>"

showNameList = ["Dai", "Juju", "Piece", "Stone", "Trigger"]
printYesNo = False

for title in titles:
    i = 1

    for showName in showNameList:
        if showName in title and "Dub" not in title:
            printYesNo = True
    titleTagged = "<title>" + title + "</title>"
    descriptionTagged = "<description>" + descriptions[i] + "</description>"
    guidTagged = "<guid>" + guidList[i] + "</guid>"
    if printYesNo == True:
        print(
                rssOpen,
                titleTagged, 
                rssLink,
                guidTagged,
                descriptionTagged,  
                rssDate,
                rssClose,
                sep='\n')
    i += 1
    printYesNo = False
