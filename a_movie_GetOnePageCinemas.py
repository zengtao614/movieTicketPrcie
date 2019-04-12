
"""
    爬取指定电影第一页所有电影院
"""

from bs4 import BeautifulSoup
import requests
import 猫眼电影票.a_movieCinemas_allScene

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

def fun(url,tbname_movie_id):
    res = requests.get(url,headers)
    html = res.content

    soup = BeautifulSoup(html,"html.parser")
    cinemas_list = soup.find_all("div",attrs={"class":"cinema-cell"})
    for cinemas in cinemas_list:
        cinemas_name = cinemas.find("a",attrs={"class":"cinema-name"}).string
        cinemas_url = cinemas.find("a",attrs={"class":"cinema-name"}).get("href")
        print(cinemas_name+":"+cinemas_url+"\n")

        猫眼电影票.a_movieCinemas_allScene.fun(cinemas_url,tbname_movie_id,cinemas_name)

# def Main():
#     url = "https://maoyan.com/cinemas?movieId=341139&offset=0"
#     analysePrice(loadPage(url))
#
# Main()

