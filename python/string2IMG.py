#-*- coding: utf-8 -*-
#base64로 받은 이미지를 파일로 만들어줍니다.
import base64
import os
import sys


#변수지정
imgNum = 0
userid = sys.argv[1]

#디렉토리 위치 변경
os.chdir('../upload')

#데이터 받기 및 해석
data = open('temp.txt', 'r').read()
data = data.replace(" ", "")
data = base64.b64decode(data + '=' * (4 - len(data) % 4));

#폴더에 사진 중복 방지 확인
while 1:
    if os.path.isfile("./" + str(userid) + "_" + str(imgNum) + ".png"):
    	imgNum = imgNum + 1
    else:
        break
        
#파일 저장 및 경로 저장
e=open(str(userid) + "_" + str(imgNum) + ".png",'wb') 
e.write(data)
e.close()

print("../upload/" + str(userid) + "_" + str(imgNum) + ".png")