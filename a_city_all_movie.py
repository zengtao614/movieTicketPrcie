
"""
    爬取指定城市所有正在热映的影片
"""

from bs4 import BeautifulSoup
import requests
import re
import 猫眼电影票.a_movie_ErgodicAllPageCinemas
import test3


headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

def loadPage(url):
    """
    向指定url地址模拟浏览器发送请求
    :param url: 指定url地址
    :return: 返回html
    """
    res = requests.get(url,headers)
    html = res.content
    return html

def analysePrice(html):
    soup = BeautifulSoup(html,"html.parser")
    movie_list_url = soup.find("dl",attrs={"class":"movie-list"})
    movies = movie_list_url.find_all("dd")

    # 数据库连接
    connection = test3.connec()
    # 创movielist表 保存电影名和电影id
    ct_sql = """CREATE TABLE movielist (
            id int auto_increment primary key,
            movieId  VARCHAR(20),
            movieName VARCHAR(20))"""
    test3.createTable(ct_sql,"movielist",connection)

    for movie in movies:
        # movie_name:电影名
        movie_name = movie.find("div",attrs={"class":"channel-detail movie-item-title"}).get("title")
        # movie_url:电影url
        movie_url = movie.find("a").get("href")
        # movie_id:电影id
        movie_id = "".join(re.findall("\d",movie_url))
        tbname_movie_id = "m"+movie_id


        cursor = connection.cursor()
        sql = 'INSERT INTO `movielist` (`movieId`,`movieName`) VALUES (%s,%s)'
        cursor.execute(sql,(tbname_movie_id,movie_name))
        connection.commit()
        # print("录入成功")

        # 创表
        ct_movie_sql = """CREATE TABLE """+tbname_movie_id+""" (
            id int auto_increment primary key,
            cinemas  VARCHAR(20),
            showday VARCHAR(20),
            showtime VARCHAR(20),
            prices VARCHAR(20))"""
        test3.createTable(ct_movie_sql,tbname_movie_id,connection)

        movie_url = "https://maoyan.com/cinemas?movieId="+movie_id
        print(movie_name+":"+movie_url+"\n")
        猫眼电影票.a_movie_ErgodicAllPageCinemas.Main(movie_url,tbname_movie_id)
    connection.close()

def Main():
    url = "https://maoyan.com/films?showType=1"
    analysePrice(loadPage(url))

Main()

