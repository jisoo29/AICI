# AICI👨‍🔧
<p align="center">
<img src="https://github.com/jisoo29/AICI/assets/120074030/daff501f-6a72-46e2-a68d-571af07ea938.png" width="300px" height="20%"/></p>
<p align="center">
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjisso29%2FAICI&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a></p>

## 프로젝트 내용
>**고객 TM 및 사외공사 신고 관리 자동화 프로세스**   
>**개발기간 : 2023 - 05 - 30 ~ 2023 - 07 - 18**
## 베포주소
>**http://52.78.234.62/**

<hr></hr>

## 프로젝트 소개
본 프로젝트는 KT의 사업부서의 과제로 효율적인 업무를 위한 자동화 시스템 AICI으로 사업 부서에서 제시한 2가지의 요구사항  
   
**1. 고객 TM확인 서비스**   
AICI 시스템으로 장애 영향 고객에 동시다발 고객 TM을 시행 후 결과를 수합하여 확인할 수 있는 서비스인 고객 TM확인 서비스를 개발      
   
**2. 사외공사 신고 서비스**   
AICI시스템으로 사외 공사를 신고하고, 관리 및 자동 응대를 시행할 수 있는 사외 공사 신고 서비스를 개발   

## Architecture
### Presentation  
<div class="badge-container">
<img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=HTML5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS3&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/></div>
   
### Application    
<div class="badge-container">
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=NGINX&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=Gunicorn&logoColor=white"/></div>  

### Database   
<div class="badge-container">
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/></div>   

<hr></hr>

## 화면구성
### 메인페이지
<img src="https://github.com/jisoo29/jisoo29/assets/120074030/e787bde3-efbf-45a5-beaa-2667358519da.png" width="600px" height="300px"/></p>
                |고객TM                          |사외공사                         
|-------------------------------|-----------------------------|
|![고객TM](https://github.com/jisoo29/jisoo29/assets/120074030/44e18e5c-2222-4cc4-a1ab-76570aa180cd) |![사외공사](https://github.com/jisoo29/jisoo29/assets/120074030/785f7f71-ce53-4ebd-88e2-a9bf1b7cf161) |   

<hr></hr>

## 주요 기능
### 고객 TM확인 서비스
- 고객 TM확인 서비스의 경우 접수된 VOC 내역과 고객 TM확인을 마친 후 수합한 응답 결과 파일 업로드   
- 응답 결과를 한 화면에 배치하여 한 눈에 파악 가능   
### 사외공사 신고 서비스   
- 사외공사자의 음성 파일을 업로드
- 신고된 사외공사에서 날짜, 담당자, 담당자 번호, 공사 위치, 공사 종류 업데이트
- 공사 위치를 알 수 있는 지도 제공
- 
<hr></hr>

## Version
- python==3.10.11
- Django==4.2.2
- gunicorn==20.1.0
 
## 디렉토리 구조
```
├── AICI_WEB                    # configuration
├── AI                          # AI
├── board                       # main page
├── construction                # construction page
├── users                       # sign in / sign up page
├── voc                         # voc page
│
├── media                       # file storage
│   ├── board                   # attatched file in board
│   └── voc                     # attatched excel file in voc
├── static
│   ├── admin
│   │   ├── css
│   │   │   └── vendor
│   │   │       └── select2
│   │   ├── img
│   │   │   └── gis
│   │   └── js
│   │       ├── admin
│   │       └── vendor
│   │           ├── jquery
│   │           ├── select2
│   │           │   └── i18n
│   │           └── xregexp
│   ├── construction
│   ├── home
│   ├── privacy
│   └── service
└── templates
    ├── board
    ├── construction
    ├── users
    └── voc
```
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=jisoo29&layout=compact)](https://github.com/jisoo29/github-readme-stats)
