tshark -i 5 -a duration:20 -w output.pcap
bash pcap2wav -r output.pcap
py sttModule.py 0out
py sttModule.py 1out
