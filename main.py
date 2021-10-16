from selenium import webdriver
import webbrowser
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import requests
from playsound import playsound
karaoke_song_number = ""
characters = "ok"
while True:
    karaoke_song_number_num = str(input("노래방 노래 번호를 입력해주세요: "))
    print(karaoke_song_number_num)
    karaoke_song_number = karaoke_song_number + karaoke_song_number_num
    if karaoke_song_number_num == "1":
            playsound("sound/1.wav")
    if karaoke_song_number_num == "2":
            playsound("sound/2.wav")
    if karaoke_song_number_num == "3":
            playsound("sound/3.wav")
    if karaoke_song_number_num == "4":
            playsound("sound/4.wav")
    if karaoke_song_number_num == "5":
            playsound("sound/5.wav")
    if karaoke_song_number_num == "6":
            playsound("sound/6.wav")
    if karaoke_song_number_num == "7":
            playsound("sound/7.wav")
    if karaoke_song_number_num == "8":
            playsound("sound/8.wav")
    if karaoke_song_number_num == "9":
            playsound("sound/9.wav")
    if karaoke_song_number_num == "ok":
        for x in range(len(characters)):
                karaoke_song_number = karaoke_song_number.replace(characters[x],"")
        print(karaoke_song_number)
        break
tj_url = "http://www.tjmedia.com/tjsong/song_search_list.asp?strCond=0&strType=0&strText={}".format(karaoke_song_number)
webpage = requests.get(tj_url)
soup = bs(webpage.content, "html.parser")
song_name = soup.select_one("td.left").string
print(song_name+ " 을 재생합니다!")
keyword = str(song_name) + " 노래방"
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
