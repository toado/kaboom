from bs4 import BeautifulSoup
from urllib.request import urlopen
from googlesearch import search


class Show:
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(openUrl(url), "html.parser")
        self.title = ""
        self.image = ""
        self.score = ""
        self.year = ""
        self.genres = []

    def getInfo(self):
        soup = self.soup

        title = soup.findAll("span", {"itemprop":"name"})
        self.title = title[0].text.strip()

        image = soup.findAll("img", {"class":"ac"})
        self.image = image[0]["src"].strip()

        score = soup.findAll("div", {"class":"fl-l score"})
        self.score = score[0].text.strip()

        year = soup.findAll("span", text="Premiered:")
        self.year = year[0].parent.a.text.split()[1]

        genresHTML = soup.findAll("span", text="Genres:")
        genresHTML = genresHTML[0].parent.findAll("a")
        for genreHTML in genresHTML:
            self.genres.append(genreHTML.text.strip())

    def printInfo(self):
        print("Title: " + self.title)
        print("Image: " + self.image)
        print("Score: " + self.score)
        print("Year: " + self.year)
        print("Genres: ", end="")
        for genre in self.genres:
            print(genre, end=" ")


def main():
    query = input("Enter the title: ")
    url = getUrl(query)

    userShow = Show(url)
    userShow.getInfo()
    userShow.printInfo()


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


if __name__ == "__main__":
    main()
