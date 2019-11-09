from bs4 import BeautifulSoup
from urllib.request import urlopen
from googlesearch import search


def main():
    query = input("Enter the title: ")
    url = getUrl(query)
    pageHTML = openUrl(url)

    soup = BeautifulSoup(pageHTML, "html.parser")
    getInfo(soup)


def getUrl(query):
    urls = []
    for result in search(query + " myanimelist", tld="com", lang="en", num=1, start=0, stop=1, pause=2.0):
        urls.append(result)
    return urls[0]


def openUrl(url):
    client = urlopen(url)
    pageHTML = client.read()
    client.close()
    return pageHTML


def getInfo(soup):
    pass


if __name__ == "__main__":
    main()
