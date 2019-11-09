#===============================================================================
'''imports'''
from googlesearch import search
from bs4 import BeautifulSoup
import urllib.request
import requests
#===============================================================================
def movie_selector():
    user_movie = input("Enter your favourite movie: ")
    query = user_movie + " rotten tomatoes"
    return query
    
def google_scraper(url):
    website = urllib.request.urlopen(url)
    soup = BeautifulSoup(website, "html.parser")
    return soup.title.text

def user_movie_choices(query):
    movie_list = []
    movie_url = [i for i in search(query, tld="com", num=10, stop=3, pause=2)]
    print (movie_url)
    correct_movie = ""
    found = False
    while found == False:
        for website in movie_url:
            print(google_scraper(website))
            movie_list = [google_scraper(website), website]
            while correct_movie not in ["Y", "N"]:
                correct_movie = input("Is this the right movie? (Y/N)").upper()
                found == True
            if correct_movie == "Y":
                return movie_list
            
                #movie_list.append([website, google_scraper(website)])
        
        #movie_list.append(google_scraper(website))
    #return movie_list
        #print(website)  

def get_rating(url):
    website = urllib.request.urlopen(url)
    soup = BeautifulSoup(website, "html.parser")
    el = soup.find(class_ = 'mop-ratings-wrap__percentage')
    #print (el)
    return el.get_text()

def get_genre(url):
    website = urllib.request.urlopen(url)
    soup = BeautifulSoup(website, "html.parser")
    el = soup.find(class_ = "meta-value")
    
    
def main():
    query = movie_selector()
    title, url = user_movie_choices(query)
    print("Title:", title)
    print("URL:", url)
    rating = get_rating(url).strip()
    print (rating) #got rating
    genre = get_genre(url)
    print (genre)
    
#===============================================================================

#using rotten tomatoes for TV shows
#assume show is valid show
#web = website.getText()
#r = requests.get(website)

#print (r)

if __name__ == "__main__":
    main()