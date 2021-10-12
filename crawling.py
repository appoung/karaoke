from selenium import webdriver
import webbrowser
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import requests
karaoke_song_number = input("노래방 노래 번호를 입력해주세요: ")
tj_url = "http://www.tjmedia.com/tjsong/song_search_list.asp?strCond=0&strType=0&strText={}".format(karaoke_song_number)
webpage = requests.get(tj_url)
soup = bs(webpage.content, "html.parser")
song_name = soup.select_one("td.left").string
keyword = song_name + " 노래방"
url = 'https://www.youtube.com/results?search_query={}'.format(keyword)

driver = webdriver.Chrome(r"C:\chromedriver.exe")
driver.get(url)
soup = bs(driver.page_source, 'html.parser')
driver.close()

name = soup.select('a#video-title')
video_url = soup.select('a#video-title')
view = soup.select('a#video-title')

name_list = []
url_list = []
view_list = []
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
for i in range(len(name)):
    name_list.append(name[i].text.strip())
    view_list.append(view[i].get('aria-label').split()[-1])
for i in video_url:
    url_list.append('{}{}'.format('https://www.youtube.com',i.get('href')))
webbrowser.get(chrome_path).open(url_list[0])
time.sleep(3)
pyautogui.hotkey('f')
