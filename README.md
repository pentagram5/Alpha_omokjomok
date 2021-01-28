# Alpha_Omokjomok - 인공지능 오목 대국프로그램
#### * 2019년 한서대학교 항공 소프트웨어 공학과 2019-A5 프로젝트 
#### * 팀원 : 201301256 김상우 201301264 김준연 201401443 이승혁 201301307 한대호   
#### * Alpha_Omokjomok은 강화학습 및 Rule 기반 인공지능 오목 대국프로그램입니다.
#### * Google Deepmind 사의 Alpha-zero를 기반으로 하여 Policy-value Network 및 MCTS 알고리즘 적용
# Requirements 및 개발환경
개발언어 : Python==3.6.10  
딥러닝/머신러닝 프레임워크 : torch,torchvision -> https://pytorch.org/ , tensorflow==2.1.0  , numpy  
게임환경 구현용 UI 라이브러리 : Pygame  
통합개발환경 ide : Pycharm  
OS : Ubuntu 18.04  

# Alpha_Omokjomok State & Pygame UI
![오목 최종화면](https://user-images.githubusercontent.com/63779100/106120190-6bb75680-6199-11eb-8bc5-3454209b4a22.JPG)  
기존 15x15의 2차원 배열로 AI를 구현해보고자 하였으나, 프로젝트 진행 중 개발환경과 H/W의 성능부족으로 8X8의 State로 환경 구축

## Omok 규칙
기존의 오목 대회나 정규 시합에서 적용되는 금수(금지된 수)에 대해 적용하기에는  
State가 충분히 작고 Agent의 학습 부담을 덜기위해 착수된 돌이 5개가 연이어서   
직선 혹은 대각선으로 연결시 해당 돌의 승리로 구현하였습니다. 

## Rule-based AI Agent 구축 
![Rulebased](https://user-images.githubusercontent.com/63779100/106120767-221b3b80-619a-11eb-99fd-6c7bb4211d27.gif)  
코드 기반으로 작용하는 Rule-based AI agent 15x15 state 구현화면입니다.  
돌이 3개 혹은 4개 이상일 경우 특정 Array 좌표에 돌을 둘수 있도록  
유리한 환경에 따라 차등적으로 조건을 선택하도록 구현


## Reinforcement Learning AI Agent vs Rule-based AI Agent

![8x8 RL vs Rule](https://user-images.githubusercontent.com/63779100/106122253-d7022800-619b-11eb-92bb-4bd5d98f4de2.gif)


## RL AI agent 성능평가
![최종결과](https://user-images.githubusercontent.com/63779100/106122489-1c265a00-619c-11eb-8b55-9f9c394604ac.JPG)  
RL(Reinforcement Learning) AI Agent는 MCTS 알고리즘을 기반으로  
자가대국(Agent vs Agent)을 통해 Policy-value network를 형성,  
자가대국 횟수별 Model를 차등적으로 저장 후, 벤치마킹 대상인 Rule 기반 Agent와의 대국을 통해 성능평가

## 2019-A05 알파 오목조목 종합프로젝트 팀원 역할


![팀원역할분담](https://user-images.githubusercontent.com/63779100/106121168-9950cf80-619a-11eb-9179-00f7f88a66ac.JPG)


AlphaGo Omok Version 
By Kim Joon Yeon, Kim Sang Woo, Lee Seung Hyeok, Han Dae Ho

Copyright 2018. Kim Joon Yeon, Kim Sang Woo, Lee Seung Hyeok, Han Dae Ho All Rights Reserved.
