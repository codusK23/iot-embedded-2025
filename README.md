# iot-embedded-2025
IoT 임베디드 시스템 리포지토리

## 1일차
### 개발 환경
#### Raspberry Pi OS 다운로드
- https://www.raspberrypi.com/software/
- 디바이스 : RASPBERRY PI 5
- 운영체제 : RASPBERRY PI OS (64bit)
- 저장소 : SD카드
- OS 커스터마이징 : 일반 - 무선랜 설정, 서비스 - SSH 사용
- 설치 후 라즈베리파이에 장착

#### Raspberrypi SSH 활성화
- Putty Host Name : raspberrypi.local -> SSH -> Open
- sudo raspi-config
- Interface Options -> SSH -> Yes

#### VNC Viewer 다운로드
- https://www.realvnc.com/en/connect/download/vnc/?lai_vid=DBj1M9KX8Hxrx&lai_sr=5-9&lai_sl=l

#### SD카드 Formatter 다운로드
- https://www.sdcard.org/downloads/formatter/
 
#### Raspberry Pi 시작하기
- sudo apt update & sudo apt upgrade -y
- sudo reboot now
- sudo raspi-config
- Interface Options -> VNC -> Yes
- 한글 설정
  1. 나눔 폰트 설치 : sudo apt install fonts-nanum fonts-nanum-extra
  2. 폰트 등록 : sudo apt install fonts-unfonts-core
  3. 터미널 한글 설정 : Raspberry Pi Configuration - Local - ko, UTF-8 설정

  <!-- - 한글 입력, 추후 수정!!
    - sudo apt install ibus
    - sudo apt install ibus-hangul -->

#### nanorc 수정
  - sudo nano /etc/nanorc 주석 해제
    - set autoindent
    - set linenumbers
    - set tabsize 4

### 파일 관련 명령어
- ls -al : 숨김 포함 파일 목록
- ls -l : 상세 파일 목록
- ls *.txt : .txt 확장자 파일 목록
. / .. : 현재 / 상위 디렉토리
~ : 홈 디렉토리


## 2일차
### 파이썬 가상환경
- 프로젝트마다 파이썬 패키지 다르기 때문에 충돌 발생 가능성 있음
- 가상환경을 만들어 독립적으로 관리
- 생성 : python -m venv --system-site-package env
- 실행 : cd env/bin -> source activate

### 라즈베리파이 5 사양
- pinout

  <img src="./Image/em0001.jpg" width="500">

  - 3.3V / 5V : 전원 공급
  - GND(Ground) : 접지
  - GPIO : 제어 신호를 주고 받는 핀

### 브레드보드

<img src="./Image/em0002.jpg" width="400">

- (+)전원 : 5V, 3.3V
- (-)접지 : GND
- 전원, 접지 가로 방향 연결
- 핀 세로 방향 5칸 연결

### 전류 흐름
- 전류가 흐르기 위해서는 반드시 전압차가 필요
- 이론적 흐름 : (+) -> (-)
- 실제 전자 흐름 : (-) -> (+)

#### 직렬연결과 병렬연결
- 직렬 : 전류가 동일, 전압은 분배
- 병렬 : 전압이 일정, 전류는 분배

#### 아날로그와 디지털
- 아날로그 : 연속적인 값을 가짐. 센서 값이나 온도처럼 변화하는 값
- 디지털 : 0 또는 1의 값만을 가짐. 이진수 기반. 스위치처럼 확실한 상태 구분

#### GPIO 제어 (RPi.GPIO 모듈)
- 핀 번호 체계 설정
  - GPIO.setmode(GPIO.BCM) : 논리 핀 번호 사용
  - GPIO.setmode(GPIO.BOARD) : 물리핀 번호 사용

- 핀 모드 설정
  - GPIO.setup(핀번호, GPIO.IN) : 입력 모드
  - GPIO.setup(핀번호, GPIO.OUT) : 출력 모드

- 입출력 제어
  - GPIO.input(핀번호) : 입력 값 읽기
  - GPIO.output(핀번호, HIGH) : 3V, 5.5V 출력
  - GPIO.output(핀번호, LOW) : 0V 출력

- 사용 후 초기화
  - GPIO.cleanup() : 사용한 핀 초기화

### 센서
#### LED
- LED RGB 모듈 140C05 사용

  <img src="./Image/em0003.jpg" width="300">

  - (V) : Vcc (+)
  - (R) : Red 
  - (B) : Blue
  - (G) : Green

- LED의 (V)가 Vcc에 연결되어 있고 GPIO를 통해 GND처럼 동작하기 때문에 LOW할 때 LED 켜짐

- [코드 실습 영상](./Day01/led.py)

  https://github.com/user-attachments/assets/609d2532-0b06-44c2-a1b4-ace349429a01
  
#### 스위치
- 버튼 스위치 모듈 KY-004 사용

  <img src="./Image/em0005.jpg" width="300">

  - (-) : GND
  - ( ) : Vcc
  - (S) : Signal

- [코드 실습 영상](./Day01/button.py)

  https://github.com/user-attachments/assets/fb5ac6c6-d7db-4689-a701-fcadba99ae39

- 풀 업 / 풀 다운 저항
  - 스위치를 누르면 GND에 닿아 입력핀이 기본값을 읽어옴
  - 풀 업 : 기본 값 1(HIGH), 스위치를 누르면 0(LOW)
  - 풀 다운 : 기본 값 0(LOW), 스위치를 누르면 1(HIGH)


 ## 3일차
 ### 센서
 #### 온습도
- 온습도 센서 모듈 DHT11 사용

  <img src="./Image/em0007.jpg" width="300">

- pip install adafruit-circuitpython-dht
- sudo apt install libgpiod2

- (-) : GND
- ( ) : Vcc - 3.3V
- (S) : Signal

#### DB에 온습도 데이터 넣기
- DB 설치
  - sudo apt install mariadb-server

- DB 접속
  - sudo mysql
  - show databases;

- root 사용자 비밀번호 설정
  - ALTER USER 'root'@'localhost' IDENTIFIED BY '비밀번호';

- DB / TABLE 생성
  - CREATE DATABASE 데이터베이스이름;
  - CREATE TABLE 테이블이름 (데이터 설명);

- 데이터 삽입
  - pip install mysql-connector-python
  ```python
  import mysql.connector

  
  db = mysql.connector.connect(
       host = "localhost",
       user = "root",
       password = "",           # 보안상 생략
       database = "TESTDB"
  )

  cursor = db.cursor()

  ...

  while True:
      try:
          cursor.execute("INSERT INTO dht11_data (temp, humi) VALUES (%s, %s)", (temp, humi))
          
          db.commit()

  ...

  ```

  - TESTDB.dht11_data

    <img src="./Image/em0008.jpg" width="400">
