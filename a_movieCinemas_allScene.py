

"""
    爬取指定电影最近几天（网页上显示的天数）所有场次选座页面url
"""

from bs4 import BeautifulSoup
import requests
import urllib.parse
import 猫眼电影票.a_price



headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

def fun(url,tbname_movie_id,cinemas_name):
    url = "https://maoyan.com"+url
    res = requests.get(url,headers)
    html = res.content

    url_parse = urllib.parse.urlparse(url)
    parameter_dic = urllib.parse.parse_qs(url_parse.query)
    url_movie_id = parameter_dic.get("movieId")[0]

    soup = BeautifulSoup(html,"html.parser")
    movie_list_html = soup.find("div",attrs={"class":"movie-list"})
    movie_list = movie_list_html.find_all("div",attrs={"class":"movie"})
    for movie in movie_list:
        movie_id = movie.get("data-movieid")
        if movie_id==url_movie_id:
            data_index=movie.get("data-index")
            movie_html = soup.find("div",attrs={"class":"show-list","data-index":data_index})

            date_url = movie_html.find("div",attrs={"class":"show-date"})
            dates = date_url.find_all("span",attrs={"class":"date-item"})
            days = 0
            for date in dates:
                day = date.string
                print(day+":\n")
                day_url = movie_html.find_all("div",attrs={"class":"plist-container"})
                price_info_url = day_url[days].find("tbody").find_all("tr")
                for number in price_info_url:
                    # try:
                    #     # time为开场时间
                    #     time = number.find("span",attrs={"class":"begin-time"}).string
                    #     # buy_url为选座购票页面url
                    #     buy_url = number.find("a",attrs={"class":"buy-btn normal"}).get("href")
                    #     complet_buy_url = "https://maoyan.com"+buy_url
                    #     猫眼电影票.a_price.fun(complet_buy_url,tbname_movie_id,cinemas_name,day,time)
                    # except:
                    #     print("没有数据\n")
                    # else:
                    #     print(time+":"+buy_url+"\n")
                    # time为开场时间
                        time = number.find("span",attrs={"class":"begin-time"}).string
                        # buy_url为选座购票页面url
                        buy_url = number.find("a",attrs={"class":"buy-btn normal"}).get("href")
                        complet_buy_url = "https://maoyan.com"+buy_url
                        猫眼电影票.a_price.fun(complet_buy_url,tbname_movie_id,cinemas_name,day,time)
                        print(time+":"+buy_url+"\n")

                days = days+1


# def Main():
#     url = "https://maoyan.com/cinema/13580?poi=6657685&movieId=1216383"
#     fun(url)
# Main()

