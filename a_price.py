
"""
    爬取对应电影指定场次的价格（选座页面）
    采用webdriver模拟浏览器
"""

from selenium import webdriver
# import re
import test3


headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
proxy = "47.95.116.95:3128"


# url = "https://maoyan.com/xseats/201903120187292?movieId=1206605&cinemaId=13580"
# 设置浏览器窗口不弹出
def getBrowser(changeProxie):
    chrome_options = webdriver.ChromeOptions()
    if changeProxie:
        chrome_options.add_argument("--proxy-server=http://" + proxy)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser

changeProxie = False

def fun(complet_buy_url,tbname_movie_id,cinemas_name,day,time):
    global changeProxie
    browser = getBrowser(changeProxie)
    browser.get(complet_buy_url)
    price_html_url = browser.find_elements_by_class_name("info-item")
    try:
        price =price_html_url[6].text
    except:
        print("正在更换代理")
        changeProxie = True
        fun(complet_buy_url,tbname_movie_id,cinemas_name,day,time)
    print(price_html_url[6].text)
    # 连接数据库
    connection = test3.connec()
    cursor = connection.cursor()
    sql = "INSERT INTO "+tbname_movie_id+"(cinemas,showday,showtime,prices) VALUES(%s,%s,%s,%s)"
    cursor.execute(sql,(cinemas_name,day,time,price))
    connection.commit()
    connection.close()





#测试
# def fun(complet_buy_url):
#     browser.get(complet_buy_url)
#     price_html_url = browser.find_elements_by_class_name("info-item")
#     for price in price_html_url:
#         print(price)
    # price =price_html_url[6].text
    # print(price_html_url[6].text)
    # # 连接数据库
    # connection = test3.connec()
    # cursor = connection.cursor()
    # sql = "INSERT INTO "+tbname_movie_id+"(cinemas,showday,showtime,prices) VALUES(%s,%s,%s,%s)"
    # cursor.execute(sql,(cinemas_name,day,time,price))
    # connection.commit()
    # connection.close()
# url = "https://maoyan.com/xseats/201903220266318?movieId=1167831&cinemaId=15780"
# fun(url)