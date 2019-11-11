def main():
    #imports/packages
    import random
    import requests
    from bs4 import BeautifulSoup
    from googlesearch import search

    def googleSearch():
        #Google search https://www.geeksforgeeks.org/performing-google-search-using-python-code/
        show_website = None
        show = input("Please enter a specific TV Show: ")
        query = "imdb " + show + ' tv'
        for x in search(query, tld="com", start = 0, stop = 1, num = 1, pause = 2.0):
            show_website = x #Get website from idmb to use for scraping.
        return show_website

    def infoScraper(show_website): #Scrape rating and genre
        info_dict = {}
        #Finding the Rating
        print('url is: ' + show_website)
        page = requests.get(show_website)
        soup = BeautifulSoup(page.content, 'html.parser')
        class_rating = soup.find(class_ = 'ratingValue') #class id for the ratings
        span_rating = class_rating.find('span') #rating span within parent class
        rating = float(span_rating.get_text()) #print spans rating.
        print("Rating is", rating, '\n')
        info_dict['Rating'] = rating

        #Finding the Genre(s)
        genres_list = []
        class_genre = soup.find(class_ = 'subtext') #class id that contains genres and "Tv-Series"
        for i in class_genre.find_all('a'): #All genres are <a href> on IMDB so we narrow it down.
            genres_list.append(i.get_text()) #Append to a list and pop the last element as TV series will always be the last one.
        genres_list.pop()
        print(genres_list)
        info_dict['Genres'] = genres_list

        return info_dict

    def recommend(information):
        #Recommend 3 shows based off genres and rating.
        randomGenre = random.choice(information['Genres'])
        print(randomGenre, '\n')
        recommendedList = []
        recommendingWebsite = requests.get('https://www.imdb.com/search/title/?genres={}&groups=top_250&sort=user_rating&title_type=feature'.format(randomGenre)) #Search the top 250 on IMDB
        recommendedSoup = BeautifulSoup(recommendingWebsite.content, 'html.parser')
        test2 = recommendedSoup.find_all(class_ = 'lister-item-image float-left') #Class ID that contains the a alt that we get the recommended movies name of
        for i in test2:
            img = (i.find('img', alt = True)) #For each <a href> add that name of the movies from alt = "Name"
            recommendedList.append(img['alt'])
        suggestion = random.choice(recommendedList[0:15]) #Pick random top 15 movies for random given genre.
        print(suggestion)



    website = googleSearch()
    scrape = infoScraper(website)
    suggestion = recommend(scrape)

main()



























