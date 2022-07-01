##  AutoTweetForTwitch
실행시키면 방송을 켰다는 트윗을 자동으로 남겨주는 프로그램<br>
<br>
## 0. AutoTweetForTwitch.py 와 data.txt 를 다운로드
둘이 같은 폴더에 넣어놓으면 됩니다.<br>
이때 스크립트와 txt는 UTF-8로 되어있어야 해요.<br>
<br>
## 1. 파이썬 3.10.x 버전 설치
https://www.python.org/<br>
설치시 Add Python 3.10 to Path 체크<br>
설치를 끝내고 다시 시작하세요.<br>
<br>
## 2. CMD를 관리자 권한으로 실행합니다.
pip install tweepy<br>
pip install beautifulsoup4<br>
하나씩 설치해줍니다.<br>
<br>
## 2-1. 이때 CMD에서 파이썬 링크를 못 찾는다면?
윈도우 + R > sysdm.cpl > 고급 탭 > 환경 변수 > 시스템 번수 ><br>
변수 이름 Path를 더블 클릭 > 파이썬 폴더들을 추가해주세요<br>
<br>
## 예시 :<br>
C:\Users\사용자\AppData\Local\Programs\Python\Python310<br>
C:\Users\사용자\AppData\Local\Programs\Python\Python310\Scripts<br>
<br>
## 3. 트위터 전송을 위해 API를 만들어야 합니다.
https://developer.twitter.com/en/apps 에 접속합니다.<br>
Create an APP > APPLY 를 클릭하면 첫 접속자는 개발자 권한 획득 과정이 시작됩니다.<br>
기본 질문 사항 - 전화번호 등록 / 이름 / 국가 / 직업 / 기관이 파생 컨텐츠 정보를 얻을 수 있게 할까? <br>
이때 직업에서 학생을 선택하면 빠르게 진행할 수 있다고는 합니다.<br>
개인적인 용도를 선택하면 200자 이상 사용 이유 작성할 수 있음(승인은 바로 된다고 함)<br>
<br>
## 4. API 발급을 위해 APP 을 제작합시다.
https://developer.twitter.com/en/portal/register/welcome<br>
전 세계적으로 고유한 APP 이름을 설정하고 제작합니다.<br>
https://developer.twitter.com/en/portal/dashboard<br>
대시보드에서 본인이 만든 프로젝트 앱의 설정으로 들어갑니다.<br>
<br>
## 5. Settings에서 권한을 설정해주어야 합니다.
User authentication settings > Set Up<br>
User authentication settings 에서 OAuth 1.0a을 선택하여 켜줍니다.<br>
그리고 OAUTH 1.0a SETTINGS에서 Read and write를 선택합니다.<br>
Callback URI / Redirect URL 및 Website URL 는 본인이 원하는 주소 기입.<br>
<br>
## 6. Key를 발급받아 줍시다.
본인 앱의 Keys and tokens 에서 <br>
Consumer Keys - API Key and Secret 와 (앱 자체의 키)<br>
Authentication Tokens - Access Token and Secret 및 <br>
Bearer Token를 발급 받을 수 있습니다. (본인 계정의 키)<br>
키를 모르겠는 경우 ReGenerate를 눌러 새로 생성해줍시다!<br>
<br>
## 6-1. API Key를 data.txt에 넣어줍니다.
REPLACE_THIS_WITH_YOUR_CONSUMER_KEY<br>
Consumer Keys - API Key<br>
REPLACE_THIS_WITH_YOUR_CONSUMER_SECRET<br>
Consumer Keys - Secret<br>
REPLACE_THIS_WITH_YOUR_ACCESS_TOKEN<br>
Authentication Tokens - Access Token<br>
REPLACE_THIS_WITH_YOUR_ACCESS_TOKEN_SECRET<br>
Authentication Tokens - Secret<br>
REPLACE_THIS_WITH_YOUR_BEARER_TOKEN<br>
Authentication Tokens - Bearer<br>
모든 키는 위를 그대로 진행했으면 관리 창에서 확인할 수 있어요<br>
<br>
## 7. data.txt를 수정합니다
본인 방송 주소<br>
https://m.twitch.tv/본인아이디<br>
<br>
트윗 내용 또한 커스텀할 수 있습니다.<br>
<br>
기본 내용 :<br>
닉네임 "님의 방송이 켜졌습니다!"<br>
"오늘의 방송은" 제목 "입니다."<br>
본인 방송 주소<br>
빨리 보러 오실거죠?<br>
<br>
위 내용을 참고하여 data.txt를 수정해주세요.<br>
혹시 제목에서 소개글이 대신 나오면 서버에서 아직 수정이 안 된 겁니다.<br>
<br>
## 8. AutoTweetForTwitch.py 를 더블 클릭하여 실행합니다.
혹은 cmd에서 현재 폴더 경로로 이동하고<br>
AutoTweetForTwitch.py 를 치면 실행됩니다.<br>
<br>
## 주의 사항 -
본 프로그램 사용에 따른 책임은 본인에게 있습니다.<br>
API 정보를 암호화하지 않고 본인 컴퓨터에 저장합니다.<br>
안전하거나, 신뢰할 수 있는 기기에서만 사용해주세요.<br>
<br>
