
from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(5)

# import time
# time.sleep(5)

url = 'https://music.bugs.co.kr/chart'
driver.get(url)
html = driver.page_source

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

song_data = []
rank = 1
songs = soup.select('#CHARTrealtime > table > tbody > tr')

for song in songs:
    title = song.select('p.title > a')[0].text

    singer = song.select('p.artist > a')[0].text

    album = song.select('a.album')[0].text

    print(title, singer, album, sep="|")
    song_data.append(['bugs', rank, title, singer, album])
    rank += 1
    
import pandas as pd
columns = ['서비스', '순위', '타이틀', '가수', '앨범']
pd_data = pd.DataFrame(song_data, columns=columns)
print(pd_data.head())
pd_data.to_excel('./saveFiles/bugs_chart.xlsx', index=False)

