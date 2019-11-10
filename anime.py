from bs4 import BeautifulSoup
from urllib.request import urlopen
from googlesearch import search
import random


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

        year = soup.findAll("span", text="Aired:")
        year = year[0].parent.text
        self.year = year.split()[3].strip()

        genresHTML = soup.findAll("span", text="Genres:")
        genresHTML = genresHTML[0].parent.findAll("a")
        for genreHTML in genresHTML:
            self.genres.append(genreHTML.text.strip())

    def recommendShows(self):
        score = round(float(self.score))

        genresList = self.genres
        random.shuffle(genresList)
        genresList = genresList[0: (len(genresList) + 1) // 2]

        genresID = []
        for genre in genresList:
            genresID.append(getUrl(genre).split("/")[5])

        genres = ""
        for ID in genresID:
            genres += f"&genre[]={ID}"

        items = self.getItems(score, genres)

        i = 0
        counter = 0
        recommend = []
        while i < 3:
            try:
                itemUrl = items[counter]["href"]
            except IndexError:
                items = self.getItems(score - 1, genres)
                counter = 0
                continue
            try:
                recommendShow = Show(itemUrl)
            except UnicodeEncodeError:
                print("UnicodeEncodeError")
                continue
            else:
                i += 1
            finally:
                counter += 1
            recommendShow.getInfo()
            recommend.append(recommendShow)

        return recommend

    def getItems(self, score, genres):
        url = f"https://myanimelist.net/anime.php?q=&type=0&score={score}&status=0&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c[]=c&gx=0{genres}"
        print(url)
        soup = BeautifulSoup(openUrl(url), "html.parser")
        items = soup.findAll("a", {"class":"hoverinfo_trigger fw-b fl-l"})
        random.shuffle(items)
        return items

    def printInfo(self):
        print()
        print("---------------------------------------------------------------")
        print("Title: " + self.title)
        print("Image: " + self.image)
        print("Score: " + self.score)
        print("Year: " + self.year)
        print("Genres: " + ", ".join(self.genres))
        print("---------------------------------------------------------------")
        print()


def main():
    random.seed()

    query = input("Enter the title: ")

    try:
        url = getUrl(query)
        userShow = Show(url)
        userShow.getInfo()
    except IndexError:
        print("Not a valid show.")
        return 1

    userShow.printInfo()

    recommendations = userShow.recommendShows()
    for recommendation in recommendations:
        recommendation.printInfo()


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