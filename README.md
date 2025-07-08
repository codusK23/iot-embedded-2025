# iot-embedded-2025
IoT 임베디드 시스템 리포지토리

## 1일차
### 개발 환경
- Raspberry Pi OS 다운로드
  - https://www.raspberrypi.com/software/
  - 디바이스 : RASPBERRY PI 5
  - 운영체제 : RASPBERRY PI OS (64bit)
  - 저장소 : SD카드
  - OS 커스터마이징 : 일반 - 무선랜 설정, 서비스 - SSH사용
  - 설치 후 라즈베리파이에 장착
 
- Raspberrypi SSH 활성화
  - Putty Host Name : raspberrypi.local -> SSH -> Open
  - sudo raspi-config
  - Interface Options -> SSH -> Yes

- VNC Viewer 다운로드
  - https://www.realvnc.com/en/connect/download/vnc/?lai_vid=DBj1M9KX8Hxrx&lai_sr=5-9&lai_sl=l

- SD카드 Formatter 다운로드
  - https://www.sdcard.org/downloads/formatter/
 
- Raspberry Pi 시작하기
  - sudo apt update & sudo apt upgrade -y
  - sudo reboot now
  - sudo raspi-config
  - Interface Options -> VNC -> Yes
  - 한글 설정
      - 나눔 폰트 설치 : sudo apt install fonts-nanum fonts-nanum-extra
      - 폰트 등록 : sudo apt install fonts-unfonts-core
      - 터미널 한글 설정 : Raspberry Pi Configuration - Local - ko, UTF-8 설정
