import urllib2
from bs4 import BeautifulSoup

#open webpage
webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague")
soup = BeautifulSoup(webpage, "html.parser")

def extractMData (webpage):
    soup = BeautifulSoup(webpage, "html.parser")
    divBlock = soup.findAll("div", {"class" : "block"})
    info = divBlock[3]
    getRight = info.findAll("div", {"class":"info_right"})
    getLeft = info.findAll("div", {"class": "info_left"})
    for i in range(0, len(getLeft)):
        textLeft = getLeft[i].get_text()
        textRight = getRight[i].get_text()
        print textLeft +": " + textRight

#Narrowing down the contents of the divs
divContainer = soup.find("div", {"id":"container"})
divBlock = divContainer.findAll("div", {"class": "block"})
divSep = divBlock[3].findAll("div", {"class": "separator"})
members = divSep[3].findAll("a")
#loop through members
for member in members:
    href = member.get("href")
    #create url to open
    url = "http://inadaybooks.com/justiceleague/" + href
    mPage = urllib2.urlopen(url)
    extractMData(mPage)
    #calls above function to print title for each page
    print("")
    
