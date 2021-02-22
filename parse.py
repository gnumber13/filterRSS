import requests
import datetime
from parsel import Selector

url = "http://www.crunchyroll.com/rss/anime?lang=enUS"
urlText = requests.get(url).text
#xmlFile = open("rss.xml", "r").read()
#sel = Selector(text=xmlFile)
sel = Selector(text=urlText)

titles = sel.xpath('//item/title/text()').getall()
descriptions = sel.xpath('//item/description/text()').getall()
guidList = sel.xpath('//item/guid/text()').getall()
pubDateList = sel.xpath('//item/pubdate/text()').getall()

rssOpen = "<item>"
rssLink = "<link>animeheaven.site</link>"
#rssGuid = "<guid>animeheaven.site</guid>"

rssDate = "<pubDate>" + datetime.datetime.now().strftime("%y-%m-%d %H:%M") + "</pubDate>"

rssClose = "</item>"

showNameList = ["Dai", "Juju", "Piece", "Stone", "Trigger", "Titan", "Swordart", "One Punch", "Boruto", "Clover", "Radiant"]
printYesNo = False

i = 0

print(titles)
for title in titles:

    print("title loop")
    for showName in showNameList:
        print("showname loop")
        if showName in title and "Dub" not in title:
            print("showname loop if")
            printYesNo = True
            titleTagged = "<title>" + title + "</title>"
            descriptionTagged = "<description>" + descriptions[i] + "</description>"
            guidTagged = "<guid>" + guidList[i] + "</guid>"
            pubDateTagged = "<pubdate>" + pubDateList[i] + "</pubdate>"
            showName = showName
            break

    if printYesNo == True:
        dateTime = datetime.datetime.now().strftime("%y%m%d%H%M%S%f")
        fileName = "items/crunchyroll/" + dateTime + "_" +  showName
        print(
                rssOpen,
                titleTagged, 
                rssLink,
                guidTagged,
                descriptionTagged,  
                pubDateTagged ,
                rssClose,
                sep='\n')

        #with open(fileName, "w") as outFile:
            #outFile.write(
                #rssOpen + "\n" +
                #titleTagged  + "\n" +
                #rssLink + "\n" + 
                #guidTagged + "\n" + 
                #descriptionTagged + "\n" + 
                #pubDateTagged + "\n" + 
                #rssClose + "\n")
    i = i + 1
    printYesNo = False
