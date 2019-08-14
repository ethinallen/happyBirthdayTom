import re
import json

import requests
from bs4 import BeautifulSoup



# the url that we are getting erotica from
url = 'https://www.lushstories.com/gay-male.aspx/9'

# the base that lets us know we have a link to a story
base = 'https://www.lushstories.com/stories/gay-male'

# the list of hrefs that we collect from the stories
links = []

# get links to stories
def getLinks():
    r = requests.get(url)
    r = r.text
    soup = BeautifulSoup(r, 'html.parser')
    # print(soup.prettify())
    theList = soup.find_all('a', href=True)
    for ref in theList:
        if ref['href'] not in links:
            if base in ref['href']:
                if '.aspx#comments' not in ref['href']:
                    links.append(ref['href'])

# get stores from links
def getSt(url):
    r = requests.get(url)
    r = r.text
    soup = BeautifulSoup(r, 'html.parser')
    kinkyWords = soup.find_all('p')
    tempList = []
    for words in kinkyWords:
        tempList.append(words.get_text(strip=True))
    return(tempList)

def makeFile():
    for link in links:
        with open('stories.json', 'a') as f:
            json.dump(getSt(link), f)

if __name__ == '__main__':
    getLinks()
    print(links)
    # tempUrl = 'https://www.lushstories.com/stories/gay-male/-the-meter-man-comes-.aspx'
    makeFile()
