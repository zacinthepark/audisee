# Seoul 01 Final Project (김민경, 박진우)

## 1. Installation

### backend

```bash
# 가상환경 생성
$ python -m venv venv

# 가상환경 활성화
$ source ./venv/Scripts/activate

# 패키지 설치
$ pip install -r requirements.txt

# migrate
$ python manage.py migrate

# loaddata
$ python manage.py loaddata movie_genres.json movies.json musics.json

# runserver
$ python manage.py runserver
```

### frontend

```bash
# npm install
$ npm i

# run serve
$ npm run serve
```

---

## 2. 프로젝트 개요

- 프로젝트 명 : **AUDISEE** (Audio + See)
- **WHY** : 영화를 즐기는 요소 중 주요한 요소 중 하나가 음악이라 생각함. 영화에 대한 추천 음악을 제공함으로써 영화를 보고난 후 음악 추천을 통해 여운을 더 느끼거나 여러 음악들을 찾아볼 수 있는 유저 경험을 제공하고자 함
- **WHAT** : 보고싶은 장르에 따른 영화 추천 및 해당 영화에 대한 음악 추천 서비스

## 3. 프로젝트 기간

- 22.11.16 ~ 22.11.24

## 4. 팀원 및 역할 분담

- 🐺 박진우 : back, front
- 🐰 김민경 : front, styling

---

## 5. Figma를 통한 초기 도안

![figma1](https://user-images.githubusercontent.com/86648892/203846688-27e9464c-40a8-4cb5-8f0a-696eaf19b5b7.png)

![figma2](https://user-images.githubusercontent.com/86648892/203846693-64f9f2bb-9a4d-4dcd-8143-aac9b691e039.png)

---

## 6. 기술 스택

### Front-end

- vue@2.7.14
- vue/cli@5.0.8
- vuex@3.6.2
- vue-router@3.6.5
- vue-slick-carousel@1.0.6
- vuex-persistedstate@4.1.0
- bootstrap-vue@2.23.1
- axios@1.1.3

### Back-end

- django@3.2.13
- djangorestframework@3.14.0
- django-cors-headers@3.13.0
- dj-rest-auth@2.2.5
- django-allauth@0.50.0

---

## 7. 핵심 기능

### a. DB 데이터 생성

- 임의의 영화 및 장르 데이터 생성을 위해 **TMDB(The Movie DataBase) API** 사용 및 fixtures 파일 생성
- 임의의 음악 장르 데이터 생성을 위해 **Spotify API** 사용 및 fixtures 파일 생성

### b. 로그인 및 회원가입 + 홈 화면

<img width="1918" alt="loginview" src="https://user-images.githubusercontent.com/86648892/203846702-e3a6eecb-e722-4a0b-bf6b-90aac0d98947.png">

<img width="1900" alt="homeview" src="https://user-images.githubusercontent.com/86648892/203846698-04f0063b-a447-49f4-92d5-a5982ce2a008.png">

- 로그인과 회원가입은 dj-rest-auth와 django-allauth을 통한 토큰 발급과 그에 따른 Token Authentication 방식을 채택
- 서비스 시작 시 로그인 및 회원가입을 우선적으로 진행해야 향후 이용이 가능하도록 설정
- 흔들리는 물결을 이용하여 영화와 음악 사이의 흐름을 나타냄

### c. 영화 검색

<img width="1878" alt="searchview" src="https://user-images.githubusercontent.com/86648892/203846739-cb1dfe22-978e-4f22-85a2-c3a3d5c076ed.png">

- 로고 및 네비게이션 바 : navigation bar에 search, members, profile 탭을 넣어서 사용자의 편의성을 도움
- 장르를 통한 영화 선택 : 여러 장르 중 하나를 선택 시 선택한 장르를 기반으로 한 영화 추천 목록으로 이동할 수 있도록 구현
- 검색어를 통한 영화 선택 : 검색어를 통해 특정 영화를 검색하는 것 역시 가능하며, 검색어를 통한 이동 시 바로 해당 영화의 상세 정보 화면으로 이동하도록 구현

### d. 영화 추천

<img width="1873" alt="recommendview" src="https://user-images.githubusercontent.com/86648892/203846736-89774d06-b3ff-4307-80a5-a0acc57cc71a.png">

- 검색 화면에서 넘겨받은 장르 데이터를 바탕으로 해당 장르에 맞는 영화 데이터들을 출력
- 해당 영화의 이미지와 제목 정보들을 담은 카드 컴포넌트를 사용하여 출력
- 관심이 가는 영화가 있을 시 해당 영화 카드를 선택할 수 있으며 이를 통해 해당 영화의 상세 정보란으로 이동

### e. 음악 추천

<img width="1873" alt="mainview1" src="https://user-images.githubusercontent.com/86648892/203846712-d6d78b2f-6523-4541-a490-542f519d39bf.png">

<img width="1758" alt="mainview2" src="https://user-images.githubusercontent.com/86648892/203846721-af7599c8-1679-4e37-a4f3-806ecd105dfb.png">

<img width="1842" alt="mainview3" src="https://user-images.githubusercontent.com/86648892/203846723-621ad4c5-dbb7-4c3a-b432-d8184d799a4b.png">

- 장르 기반 추천 영화 선택 혹은 검색어를 통한 이동 시 해당 영화 제목, 개봉일시, 평점, 간략한 줄거리 정보 출력
- 추천음악 탭 선택 시 해당 영화를 바탕으로 한 50개의 음악을 카드 형태 및 swipe 기능을 통해 추천
- 새로고침 버튼 클릭 시 새로운 음악 추천 정보 출력
- vue-slick-carousel 라이브러리를 import해 swipe가 도입된 carousel을 이용해서 음악 정보를 나타냄
- 영화 및 음악 좋아요 기능을 통해 정보 하기의 하트 버튼을 클릭 시 자신의 플레이리스트 프로필 목록에 추가
- 상세정보 탭 선택 시 Youtube API를 통해 해당 영화의 예고편 재생 가능
- 상세정보 탭 선택 시 함께 출력되는 리뷰 작성란에 리뷰 작성 및 해당 영화에 저장된 리뷰 목록을 실시간으로 출력

### f. My Profile

<img width="1811" alt="myprofile1" src="https://user-images.githubusercontent.com/86648892/203846734-2b31deb6-9ce9-4bbb-81ff-83603966e4f2.png">

<img width="1817" alt="myprofile2" src="https://user-images.githubusercontent.com/86648892/203846735-4ec920b0-2820-47c1-a0b9-4a3698d4f143.png">

- 좋아요 기능을 통해 선택한 영화 및 음악 정보들을 조회 및 출력
- 좋아요한 영화 및 음악 개수 정보, 각 영화 및 음악들의 이미지 및 제목 출력
- 영화 및 음악 삭제 기능을 통해 각 카드 하기의 삭제 버튼을 클릭 시 플레이리스트 프로필에서 실시간으로 삭제

### g. Member Profiles

<img width="1827" alt="membersview" src="https://user-images.githubusercontent.com/86648892/203846733-cbbb8605-016b-4c1a-91f1-062670805174.png">

<img width="1870" alt="memberprofile1" src="https://user-images.githubusercontent.com/86648892/203846727-c22316df-f257-4fb8-9ee8-ce14db30c978.png">

<img width="1867" alt="memberprofile2" src="https://user-images.githubusercontent.com/86648892/203846729-995796e1-80ec-4f81-ba3c-8392dab8d573.png">

<img width="1868" alt="memberprofile3" src="https://user-images.githubusercontent.com/86648892/203846731-d47bebed-dfe9-4780-ac7f-3c9d8b73f7ec.png">

- 추천 기능을 통해 영화 및 음악 추천을 받을 수도 있지만 다른 유저들의 기호를 통해 정보를 얻을 수 있다는 생각을 바탕으로 멤버 페이지 구현
- 네비게이션 바의 Members 탭을 통해 카드 컴포넌트를 통해 출력된 서비스 유저 목록 조회 가능
- 관심이 가는 유저를 클릭 시 해당 유저의 프로필 페이지로 이동할 수 있으며, 해당 유저가 좋아요했던 영화 및 음악들을 조회 가능

---

## 8. 향후 고도화 계획 및 느낀점

- 음악 미리듣기 기능을 통해 추천된 음악을 잠깐 들어봄으로써 유저로 하여금 더 마음에 드는 음악 목록을 작성할 수 있도록 서비스 제공
- 영화를 기반으로 음악 추천에서 더 나아가 특정 음악을 선택 시 반대로 해당 기호를 바탕으로 한 영화 추천
- 추천 알고리즘 고도화 (유저별 좋아요 데이터를 바탕으로 한 추천 등)
- 프로필 이미지 업로드 기능

- 느낀점 (진우) : 좋은 기획은 개발에 드는 시간을 많이 단축시켜줄 수 있음을 체감할 수 있는 시간이었다. 데이터 모델링을 변경하거나, 전체적인 플로우 및 프로젝트 구조에 변경이 가해지는 경우 개발 시간이 배로 들 수 있다. 그리고 무엇보다 좋은 기획과 아이디어는 개발에 대한 동기부여를 확실히 해주는 것 같다. 영화에 대한 음악 추천이라는 아이템 자체가 매력적으로 느껴져서 그래도 흥미를 가지고 작업한 것 같다. 또한 일주일이 조금 넘는, 짧다면 짧은 시간이긴 했지만 소규모 협업 경험을 통해 협업 과정에서 필요한 의견 교환 및 작업 방식에 대해 배울 수 있었던 시간이었던 것 같다.
- 느낀점 (민경) : 혼자 하는 프로젝트랑 팀원과 함께하는 프로젝트는 또 다른 세상이었다. 내가 부족한 부분을 진우님이 많이 메워주셔서 좋았다. 다시 하면 잘 할 수 있을 것 같다. 다음 프로젝트 진행이 기대가 된다. 구현하고자 하는 기능에 대한 욕심은 많았는데 막상 실력과 시간이 부족해서 구현하지 못한 것이 아쉽다. 그래도 생각 이상으로 잘 나오는 기능에 대해서는 뿌듯함이 느껴지기도 했다. 거인의 어깨에 올라탈 수 있어서 행복했다.
---

Consistency Wins :)
