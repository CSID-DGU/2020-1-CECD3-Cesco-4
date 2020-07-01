<h1 align="center">Sniffing 기법을 이용한 VoIP 녹취(STT) 및 회의록 생성 서비스 </h1>
<p>
</p>

> Sniffing 기법을 사용하여 VoIP 상 전달되는 패킷을 통해 회의록을 생성해주는 서비스

## Dependency
    apt-get install -y tshark sox
    or
    yum install wireshark sox
tshark, wireshark: 패킷 캡쳐 및 페이로드 분리 툴

sox(Sound eXchange): 음성 인코딩 툴

## Usage: pcap2wav
    pcap2wav [ -h|--help ]
    pcap2wav -r|--read <pcap file> [-m|--mix] [-p|--path]

--read, -r <pcap file>  : pcap file 입력
  
--mix, -m               : 두 음성 파일을 통합하여 출력

--path, -p              : 출력 경로 설정

EXAMPLES:

    pcap2wav --help
    
    pcap2wav -r example.pcap
    
    pcap2wav -r example.pcap -p /root/wav
    
    pcap2wav -r example.pcap -p /root/wav --mix

## 팀원

👤 **정동민**

* Github: [@DongMinJ](https://github.com/adsad100)

👤 **유승우**

* Github: [@seung-woo-ryu](https://github.com/seung-woo-ryu)

👤 **진영기**

* Github: [@YOUNGKI JIN](https://github.com/hankJIN)

👤 **강건**

* Github: [@lsimaru](https://github.com/lsimaru)
