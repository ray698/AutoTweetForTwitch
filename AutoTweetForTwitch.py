from encodings import utf_8
from time import time, sleep
from bs4 import BeautifulSoup
import requests, urllib, tweepy

# 헤더 정보
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"}

#정보가 들어있는 파일 경로
file_path = "./data.txt"

#파일을 읽어서 f에 저장한다.
f = open(file_path, "r", encoding="UTF8")

#data 리스트를 선언해줌
data = []

#리스트 안에 띄어쓰기 삭제해서 하나씪 넣기
while True:
    line = f.readline().strip()
    if not line: break
    data.append(line)

#트위터 설정
api = tweepy.Client(bearer_token=data[5], consumer_key=data[1], consumer_secret=data[2], access_token=data[3], access_token_secret=data[4])

#크롤링하여 저장
html = requests.get(data[0], headers=headers)
soup = BeautifulSoup(html.text, "html.parser")

# 크롤링 한 정보 중에 필요한 정보 찾기 (닉네임 제목 주소)
NickName = soup.select_one('meta[property="og:title"]')["content"]
VideoTitle = soup.select_one('meta[property="og:description"]')["content"]
Link = soup.select_one('meta[property="og:url"]')["content"]

# 닉네임 우측의 - Twitch 삭제
NickName = NickName.replace(" - Twitch", "").strip()

# 트윗을 올리기 전에 문장 완성하기
tmp = NickName + " " + data[6] + "\n" + data[7] + " " + "\"" + VideoTitle + "\"" + data[8] + "\n" + Link + "\n" + data[9]
tweet = tmp

#트윗 올리기
api.create_tweet(text=tweet)

#직관적인 안내
print("아래의 트윗을 올렸습니다.\n")
print(tweet)
print("\n")

#트윗을 올렸으면 안내해주고 종료하기
while True:
    n = input('Enter Key를 눌러 종료하세요!')
    if n == '':
        break;
