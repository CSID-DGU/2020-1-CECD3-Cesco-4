<h1 align="center">Sniffing 기법을 이용한 VoIP 녹취(STT) 및 회의록 생성 서비스 </h1>
<p>
</p>

> Sniffing 기법을 사용하여 VoIP 상 전달되는 패킷을 통해 회의록을 생성해주는 서비스

## Dependency
#### Scikit-learn  
    pip install scikit-learn
키워드 분석시 사용한 패키지 
#### konlpy, kss  
    pip install konlpy  
    pip install kss
문장 단위 분리, 단어 단위 분리시 사용한 패키지 
#### Networkx 
    pip install networkx
가중치 그래프 시각화에 필요한 패키지  
#### Google cloud STT API
    pip install google-cloud-speech
STT 기능 사용시 필요한 Google cloud STT 패키지, 설정 방식은 https://cloud.google.com/speech-to-text/docs/?hl=ko 참고
#### Python-docx
    pip install python-docx
최종 회의록 작성시 Word 파일 접근에 필요한 패키지 
   
## Usage: Main
	MeetingLog.bat 파일 실행  
파일 실행시 진행중인 VoIP 환경에서 Sniffing 실행  
패킷에서 추출한 Payload는 payload 폴더에 저장, 최종 회의록 파일은 word 폴더에 저장

## 팀원

👤 **정동민**

* Github: [@DongMinJ](https://github.com/adsad100)

👤 **유승우**

* Github: [@seung-woo-ryu](https://github.com/seung-woo-ryu)

👤 **진영기**

* Github: [@YOUNGKI JIN](https://github.com/hankJIN)

👤 **강건**

* Github: [@lsimaru](https://github.com/lsimaru)
