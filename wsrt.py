#===============================================================================
'''imports'''
from googlesearch import search
from bs4 import BeautifulSoup
import urllib.request
import requests
import random
#===============================================================================
def movie_selector():
    user_movie = input("Enter your favourite movie: ")
    query = "rotten tomatoes" + user_movie + "movie"
    return query
    
def google_scraper(url):
    website = urllib.request.urlopen(url)
    soup = BeautifulSoup(website, "html.parser")
    return soup.title.text

def user_movie_choices(query):
    movie_list = []
    movie_url = [i for i in search(query, tld="com", num=10, stop=3, pause=2)]
    print (movie_url)
    found = False
    while found == False:
        for website in movie_url:
            correct_movie = ""
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
    el = soup.find_all(class_="meta-value")
    #print("THIS IS 0:", el[0])
    #print("THIS IS 1:", el[1])
    #print("THIS IS 2:", el[2])
    print("This is el: ", el)
    string_genre = el[1].get_text()
    #print("this is string_genre", string_genre)
    clean_genre = string_genre.replace(" ", "")
    clean_genre = clean_genre.split(",")
    final_genre = [genre.strip() for genre in clean_genre]
    return(final_genre)

def get_top_url(genre):
    
    

    
def main():
    query = movie_selector()
    title, url = user_movie_choices(query)
    print("#" + "=" * 79)
    print("Title:", title)
    print("URL:", url)
    rating = get_rating(url).strip()
    print ("This is the rotten tomatoes rating:", rating) #got rating
    genre = get_genre(url)
    print (genre) #got genre
    
#===============================================================================

#using rotten tomatoes for TV shows
#assume show is valid show
#web = website.getText()
#r = requests.get(website)

#print (r)

if __name__ == "__main__":
    main()