import os
import time
from glob import glob
#from sttExample2 import googleSTT  
from googleSTT import googleSTT  
import keywords

class watchdog:
    def __init__(self):
        self.ipDict = dict()
        self.OldFileList = list()
        self.checkCount = 0
        self.NewFileList = list()
    def run(self):
        try:
            os.system(r'start /b sniffing.exe 2 ')
            self.OldFileList = glob("./payload/*")
            google = googleSTT()
            print("Start...")
            while True: # 무한 루프
                self.NewFileList = glob("./payload/*")
                SubFileList = list(set(self.NewFileList) - set(self.OldFileList))
                
                if SubFileList:
                    self.OldFileList = self.NewFileList

                    for fileListName in SubFileList:
                        self.checkCount = 0
                        ip, text = google.run(fileListName.split("\\")[-1])
                        if ip in self.ipDict:
                            self.ipDict[ip] += text
                        else:
                            self.ipDict[ip] = text
                     
                time.sleep(5) # 1초 마다 대상 디렉토리 감시
                self.checkCount += 1
                if self.checkCount > 6: # 30초 넘게 새로운 파일이 없다면
                    print("추가 생성된 파일이 없으므로 종료...")
                    text = " "
                    for key in self.ipDict.keys():
                        text += self.ipDict[key]
                    keywords.extract(text)
                    os.system(r'taskkill /im project.exe /f')
                    return
                
        except KeyboardInterrupt as e: # 사용자에 의해 "ctrl + z" 발생시
            print ("감시 중지...")

if __name__ == "__main__":
    WATCHDOG = watchdog()
    WATCHDOG.run()

    os.startfile("./word/minutes.docx")


