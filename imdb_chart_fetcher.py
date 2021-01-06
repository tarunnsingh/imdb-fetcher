from pandas.io import json
import requests
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys


HEADERSLATEST = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Accept-Language':'en-GB,en-US;q=0.9,en;q=0.8',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'})

class Scrapper():
    def __init__(self, base_url, item_count):
        self.base_url = base_url
        self.item_count = item_count
        

    def get_urls_from_movie_page(self):
        df = pd.DataFrame(columns= ['SNO', 'url'])
        page = requests.get(self.base_url, headers=HEADERSLATEST)
        soup = BeautifulSoup(page.content, features='lxml')  
        movie_table = soup.find("tbody", class_="lister-list")
        list_items = movie_table.find_all('tr')
        
        for i, item in enumerate(list_items):
            if(i < int(self.item_count)):
                link_wrapper= item.find("td", class_="titleColumn")
                link_tag = link_wrapper.find("a",  href=True)
                link = link_tag['href']
                df = df.append({'SNO': i, 'url': 'https://www.imdb.com/' + str(link)}, ignore_index=True)
                
        df.to_csv('./movie_url_list/moview_url_list.csv', index=False)
        # print("Saved {} URLs to CSV.".format(self.item_count))

    def get_movie_details(self):
        result = []
        df = pd.read_csv('./movie_url_list/moview_url_list.csv')
        all_urls = df['url']
        for i, url_ in enumerate(all_urls):
            page = requests.get(url_, headers=HEADERSLATEST)
            soup = BeautifulSoup(page.content, features='lxml')
            
            title = ''
            movie_release_year = ''
            imdb_rating = ''
            summary = ''
            duration = ''
            genre = ''

            # get title and release year
            title_wrapper = soup.find("div", class_="title_wrapper")
            title_year = title_wrapper.find("h1").text.strip()
            title = title_year.split('(')[0].strip()
            movie_release_year = title_year.split('(')[1][:-1]
            
            # get duration and genre
            sub_text = title_wrapper.find("div", class_="subtext")
            duration = sub_text.find("time").text.strip()
            genre_tags = sub_text.find_all("a", text=True)
            for genre_tag in genre_tags[:-1]:
                genre += genre_tag.text.strip() + ' '
            genre = genre.rstrip()
            genre = genre.replace(" ", ", ")
            # get imdb
            imdb_rating = soup.find("span", itemprop="ratingValue").text.strip()
            
            # get summary
            summary = soup.find("div", class_="summary_text").text.strip()
            
            result.append({
                "title": title, 
                "movie_release_year": movie_release_year, 
                "imdb_rating": imdb_rating,
                "summary": summary,
                "duration": duration,
                "genre": genre
                })

        result = json.dumps(result)
        return result
    

if __name__ == "__main__":
    base_url = sys.argv[1]
    item_count = sys.argv[2]
    scrapper = Scrapper(base_url, item_count)
    try: 
        scrapper.get_urls_from_movie_page()
    except:
        print("Something went Wrong in Collecting the Movie URLs.")
    try:
        output = scrapper.get_movie_details()
        #Saving JSON as CSV
        df = pd.read_json(output)
        df.to_csv('./movie_records/movie_records.csv', index=False)
        #Printing results to console
        print(output)
    except: 
        print("Something Went Wrong in Scrapping the details from IMDB Website.")