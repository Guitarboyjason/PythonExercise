import requests
from bs4 import BeautifulSoup 
import re
import csv

csv_filename = "instagram_random.csv"

csv_open = open(csv_filename,"w+",encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(('title','image_url'))

crawling_url = "https://www.instagram.com/p/COUqI1lnnP1/"
response = requests.get(crawling_url)

# 4)BeautifulSoup 객체 선언
bs = BeautifulSoup(response.text, 'html.parser' )

# 5)필요한 아이템 목록 가져오기
list = bs.find_all('div', {'class': "C4VMK"})

# 6)반복문 통해 필요한 속성값 분리해 받고 csv 파일로 저장
for name in list:
  h3_title = name.find_all("_6lAjh ")
  #print("h2_title=", end=""), print(h2_title)
  real_title = h3_title.text
  print(real_title)
  #print("real h2 = ",end=""), print(real_title)
  csv_writer.writerow( (real_title )

csv_open.close()
