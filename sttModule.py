import sys
import requests

#클래스 info 선언 
class recodeInfo:
    def __init__(self,fileRute, source, time):
        self.fileRute = fileRute
        self.source = source
        self.time = time
        #print("{0}가 입력됨".format(self.fileRute))

        #API부분구현필요

#전역변수 list선언 
#(1Pass에 STT까지 진행, 저장하는 경우 리스트 선언없이 입출력변경으로 해결)

#파일 입력 
def readFile(file, recodeInfoList):
    sourceFile = open(file,"r", encoding="utf8")
    while True:
        line = sourceFile.readline()
        if not line:
            break
        #,단위로 split
        lineSplit = line.split(' ')
        recodeInfoList.append(recodeInfo(lineSplit[0],lineSplit[1],lineSplit[2]))
        #입력완료.
    sourceFile.close()
    return recodeInfoList
        
#STT API 부분 
#Naver STT사용
def stt(musicPath):
    client_id = "6apmi3k1g2"
    client_secret = "YreKRO7CRIOSin6KHCmWQVfi3h34DqxsAKe8xCeO"
    lang = "Kor" # 언어 코드 ( Kor, Jpn, Eng, Chn )
    url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
    data = open(musicPath, 'rb')
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
        "Content-Type": "application/octet-stream"
    }
    response = requests.post(url,  data=data, headers=headers)
    rescode = response.status_code
    return response.text, rescode

def sttMgr(fileRute, recodingFile):
    # recodeInfoList for문
    # textForNLP = ''
    textForRecoding = ''

    #for i in recodeInfoList:
    #    tmpTxt, rescode = stt('./' + i.fileRute)
    #    if(rescode == 200):
            # textForNLP += tmpTxt +'\n'
    #        textForRecoding += '[' + i.source + '] ' + '[' + i.time + '] ' + tmpTxt +'\n'
    #    else:
            # textForNLP = 'This file is error. Error file name: ' +  i.fileRute + '. Error code: ' + rescode +'\n'
    #        textForRecoding = 'This file is error. Error file name: ' +  i.fileRute + '. Error code: ' + rescode +'\n'

    tmpTxt, rescode = stt('./' + fileRute + '.wav')
    if(rescode == 200):
        textForRecoding += tmpTxt +'\n'
    else:
        textForRecoding = 'This file is error. Error file name: ' +  fileRute + '. Error code: ' + rescode +'\n'


    # writedata.py
    # f = open('./'+ nlpFile +'.txt', 'w')
    # f.write(textForNLP)
    # f.close()
    
    f = open('./'+recodingFile +'.txt', 'w')
    f.write(textForRecoding)
    f.close()


#main
if __name__ == "__main__":

    fileName = sys.argv[1]
    rcdInfoList = []
    #readFile(fileName, rcdInfoList)
    outputFile = fileName 
    #nlpFile = "nlpFile"
    sttMgr(fileName, outputFile)