#===============================================================================
'''imports'''
from googlesearch import search
from bs4 import BeautifulSoup
import urllib.request
import requests
import random
#===============================================================================
#Title, image, score, genre, year
line = "#" + "="*79
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
    #print (movie_url)
    found = False
    while found == False:
        movie_url = [i for i in search(query, tld="com", num=1, stop=1, pause=2)]
        for website in movie_url:
            print(google_scraper(website))
            movie_list = [google_scraper(website), website]
            return movie_list
            #correct_movie = ""
            #while correct_movie not in ["Y", "N"]:
                #correct_movie = input("Is this the right movie? (Y/N)").upper()
                #found == True
            #if correct_movie == "Y":
                #return movie_list
            #print("Please be more specific.")
            #movie_url = [i for i in search(query, tld="com", num=10, stop=1, pause=2)]
            
            
                #movie_list.append([website, google_scraper(website)])
        
        #movie_list.append(google_scraper(website))
    #return movie_list
        #print(website)  

def get_rating(url):
    website = urllib.request.urlopen(url)
    soup = BeautifulSoup(website, "html.parser")
    el = soup.find(class_ = 'mop-ratings-wrap__percentage')
    #print (el)
    return el.get_text().strip()

def get_genre(url):
    website = urllib.request.urlopen(url)
    soup = BeautifulSoup(website, "html.parser")
    el = soup.find_all(class_="meta-value")
    string_genre = el[1].get_text()
    clean_genre = string_genre.replace(" ", "")
    clean_genre = clean_genre.split(",")
    final_genre = [genre.strip() for genre in clean_genre]
    return(final_genre)

def get_top_url(genre):
    sp_suffix = {
        "Kids&Family"           :"/top_100_kids__family_movies/",
        "Musical&PerformingArts":"/top_100_musical__performing_arts_movies/",
        "Mystery&Suspense"      :"/top_100_mystery__suspense_movies/",
        "Sports&Fitness"        :"/top_100_sports__fitness_movies/",
        "ArtHouse&International":"/top_100_art_house__international_movies/",
        "Action&Adventure"      :"/top_100_action__adventure_movies/",
        "ScienceFiction&Fantasy":"/top_100_science_fiction__fantasy_movies/"        
        }
    random_num = random.randrange(len(genre))
    selected_genre = genre[random_num]
    if selected_genre in sp_suffix:
        return "https://www.rottentomatoes.com/top/bestofrt" + sp_suffix[selected_genre]
    else:
        #/top_100_horror_movies/
        return "https://www.rottentomatoes.com/top/bestofrt/top_100_" + selected_genre.lower() + "_movies/"
    
def get_suggestions(url):
    movies = []
    counter = 0 
    start = False
    website = urllib.request.urlopen(url)
    soup = BeautifulSoup(website, "html.parser")
    for web in soup.find_all("tr"):
        item = web.get_text()
        #print(item)
        item = web.get_text().strip()
        item = item.replace(" ", "")
        item = item.replace("\n", "")
        item = item[:item.find(".")+1] + item[item.find("%")+1:item.rfind(")")+1]
        if item[:2] == "1.":
            start = True
        if item[:4] == "50.":
            start = False
        if start == True:
            movies.append(item)
    movies = [i[i.find(".") + 1:] for i in movies]
    #movies = [i[:i.find("(")] + " " + i[i.find("("):] for i in movies]
    movies = [i for i in movies if i]
    #print(movies)
    return movies
    
def get_suggested_movies(listg):
    movies = random.sample(listg,3)
    return movies

class MovieInformation:
    def __init__(self, title, score, genre, year, image):
        self.title = title
        self.image = image 
        self.score = score
        self.genre = genre
        self.year  = year
    def __str__(self):
        return f"{line}\nTitle: {self.title}\nScore: {self.score}\nCover URL: {self.image}\nGenre(s): {self.genre}\nYear: {self.year}\n{line}\n"
    
def get_year(title):
    return title[title.rfind('('): title.rfind(')') + 1]
        
def get_image(url):
    website = urllib.request.urlopen(url)
    soup = BeautifulSoup(website, "html.parser")
    #b = soup.a[center]
    el = soup.find_all(class_="movie-thumbnail-wrap")
    img = el[0].div.img["data-src"]
    #print(img)
    return img

    #for i in el:
        #print(i.data-srcset)
    #("data-srcset")
    #print (b)
    #print (image)
        
def main():
    query = movie_selector()
    title, url = user_movie_choices(query)
    print("This is the year:", get_year(title))
    print(line)
    print("Title:", title)
    print("URL:", url)
    rating = get_rating(url)
    print ("Rotten tomatoes' rating:", rating) #got rating
    genre = get_genre(url)
    string_genre = ", ".join(genre)
    print ("The genre(s) for this movie:", string_genre) #got genre
    topurl = get_top_url(genre)
    #print(topurl)
    suggestions = get_suggestions(topurl)
    #print("This is get_image:", get_image(url))
    #print (suggestions)
    m1, m2, m3 = get_suggested_movies(suggestions)
    print ("Suggested movies:")
    #title, score, genre, year, image = None
    sm1title, sm1url = user_movie_choices("rotten tomatoes " + m1 + " movie")
    sm2title, sm2url = user_movie_choices("rotten tomatoes " + m2 + " movie")
    sm3title, sm3url = user_movie_choices("rotten tomatoes " + m3 + " movie")
    smovie1 = MovieInformation(m1, get_rating(sm1url), ", ".join(get_genre(sm1url)), get_year(sm1title), get_image(sm1url))
    smovie2 = MovieInformation(m2, get_rating(sm2url), ", ".join(get_genre(sm2url)), get_year(sm2title), get_image(sm2url))
    smovie3 = MovieInformation(m3, get_rating(sm3url), ", ".join(get_genre(sm3url)), get_year(sm3title), get_image(sm3url))
    
    print(smovie1)
    print(smovie2)
    print(smovie3)
    
#===============================================================================

#using rotten tomatoes for TV shows
#assume show is valid show
#web = website.getText()
#r = requests.get(website)

#print (r)

if __name__ == "__main__":
    main()