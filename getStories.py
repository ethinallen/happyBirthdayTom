import requests
from bs4 import BeautifulSoup


url = 'https://www.lushstories.com/gay-male.aspx/9'

#
def getLinks():
    r = requests.get(url)
    r = r.text
    soup = BeautifulSoup(r, 'html.parser')
    theList = soup.find_all('a', href=True)
    print(theList)

if __name__ == '__main__':
    getLinks()
