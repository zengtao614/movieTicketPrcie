

"""
    爬取指定电影所有电影院页面（选电影院页面，，多页）
"""

from bs4 import BeautifulSoup
import requests
import 猫眼电影票.a_movie_GetOnePageCinemas

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
    all_page_url = soup.find("ul",attrs={"class":"list-pager"})
    all_page = all_page_url.find_all("a")
    return all_page


def Main(url,tbname_movie_id):
    猫眼电影票.a_movie_GetOnePageCinemas.fun(url,tbname_movie_id)
    all_page = analysePrice(loadPage(url))
    for page in all_page:
        if "下一页"==page.string:

            url = "https://maoyan.com/cinemas"+page.get("href")
            Main(url,tbname_movie_id)

# url = "https://maoyan.com/cinemas?movieId=341139"
# Main(url,"m341139")

