# -*- coding: utf-8 -*-
"""
import pyautogui

size=pyautogui.size() # 현재 화면의 스크린 사이즈를 가져옴
print(size)
# size[0] : width
# size[1] : height
"""
"""
import pyautogui

# 절대 좌표로 마우스 이동
#pyautogui.moveTo(200,100) # 지정한 위치(가로 x, 세로 y)로 마우스 이동
#pyautogui.moveTo(100,200,duration=5) # 5 초 동안 100, 200 위치로 이동

#pyautogui.moveTo(100,100,duration=0.25)
#pyautogui.moveTo(200,200,duration=0.25)
#pyautogui.moveTo(300,300,duration=0.25)

# 상대 좌표로 이동 (현재 커서가 있는 위치로부터)
pyautogui.moveTo(100,100,duration=0.25)
print(pyautogui.position()) # Point(x,y)
pyautogui.move(100,100,duration=0.25) # 100, 100 기준으로 +100, +100 -> 200, 200
print(pyautogui.position()) # Point(x,y)
pyautogui.move(100,100,duration=0.25) # 200, 200 기준으로 -> 300, 300
print(pyautogui.position()) # Point(x,y)

p=pyautogui.position()
print(p[0],p[1]) # x, y
print(p.x,p.y) # x,y
"""
"""
import pyautogui
#pyautogui.sleep(3) # 3초 대기
#print(pyautogui.position())

#pyautogui.click(11,53,duration=1) # 1초 동안 (64,17) 좌표로 이동 후 마우스 클릭
#pyautogui.click()
#pyautogui.mouseDown()
#pyautogui.mouseUp()

#pyautogui.doubleClick()
#pyautogui.click(clicks=500)

#pyautogui.moveTo(200,200)
#pyautogui.mouseDown() # 마우스 버튼 누른 상태
#pyautogui.moveTo(300,300)
#pyautogui.mouseUp() # 마우스 버튼 땐 상태

pyautogui.sleep(3) # 3초 대기
#pyautogui.rightClick()
#pyautogui.middleClick()

#print(pyautogui.position())
#pyautogui.moveTo(1232,464)
#pyautogui.drag(100,0) # 현재 위치 기준으로 x 100 만큼,y 0 만큼 드래그
#pyautogui.drag(100,0,duration=0.25) # 너무 빠른 동작으로 drag 수행이 안될때는 duration 을 설정
#pyautogui.dragTo(1532,464,duration=0.25) # 절대 좌표 기준으로 x 1532 , y 464 로 드래그

pyautogui.scroll(300) # 양수이면 위 방향으로, 음수이면 아래 방향으로 300만큼 스크롤
"""
"""
import pyautogui

#pyautogui.FAILSAFE=False
pyautogui.PAUSE=1 # 모든 동작에 1초씩 sleep 적용
#pyautogui.mouseInfo()

for i in range(5):
    pyautogui.move(100,100)
"""
"""
import pyautogui

# 스크린 샷 찍기
#img=pyautogui.screenshot()
#img.save("screenshot.png") # 파일로 저장

#pyautogui.mouseInfo()
#11,5 250,250,250 #FAFAFA

pixel=pyautogui.pixel(11,5)
print(pixel)

print(pyautogui.pixelMatchesColor(11,5,(250,250,250)))
print(pyautogui.pixelMatchesColor(11,5,pixel))
print(pyautogui.pixelMatchesColor(11,5,(251,250,250)))
"""
"""
import pyautogui

#file_menu=pyautogui.locateOnScreen("file_menu.png")
#print(file_menu)
#pyautogui.click(file_menu)

#trash_icon=pyautogui.locateOnScreen("trash_icon.png")
#pyautogui.moveTo(trash_icon)

#screen=pyautogui.locateOnScreen("screenshot.png")
#print(screen)

#for i in pyautogui.locateAllOnScreen("checkbox.png"):
    #print(i)
    #pyautogui.click(i,duration=0.25)

#checkbox=pyautogui.locateOnScreen("checkbox.png")
#pyautogui.click(checkbox)

#trash_icon=pyautogui.locateOnScreen("trash_icon.png")
#pyautogui.moveTo(trash_icon)

# 속도 개선
# 1. GrayScale
#trash_icon=pyautogui.locateOnScreen("trash_icon.png",grayscale=True)
#pyautogui.moveTo(trash_icon)

# 2. 범위 지정
#trash_icon=pyautogui.locateOnScreen("trash_icon.png",region=(2410,787,2513-2410,934-787))
#pyautogui.moveTo(trash_icon)

# 3. 정확도 조정
#run_btn=pyautogui.locateOnScreen("run_btn.png",confidence=0.9) # 90%
#pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
#file_menu_notepad=pyautogui.locateOnScreen("file_menu_notepad.png")
#if file_menu_notepad:
    #pyautogui.click(file_menu_notepad)
#else:
    #print("발견 실패")

#while file_menu_notepad is None:
    #file_menu_notepad=pyautogui.locateOnScreen("file_menu_notepad.png")
    #print("발견실패")

#pyautogui.click(file_menu_notepad)
# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

timeout=10 # 10 초 대기
#start=time.time() # 시작 시간 설정

# file_menu_notepad=None
# while file_menu_notepad is None:
#     file_menu_notepad=pyautogui.locateOnScreen("file_menu_notepad.png")
#     end=time.time() # 종료 시간 설정
#     if end-start>timeout: # 지정한 10 초를 초과하면
#         print("시간 종료")
#         sys.exit()

def find_target(img_file,timeout=30):
    start=time.time()
    target=None
    while target is None:
        target=pyautogui.locateOnScreen(img_file)
        end=time.time()
        if end-start>timeout:
            break
    return target

def my_click(img_file,timeout=30):
    target=find_target(img_file,timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}).Terminate program.")
        sys.exit()
# pyautogui.click(file_menu_notepad)

my_click("file_menu_notepad.png",10)
"""
"""
import pyautogui

# fw=pyautogui.getActiveWindow() # 현재 활성화 된 창 
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기 정보 (width,height)
# print(fw.left,fw.top,fw.right,fw.bottom)
# pyautogui.click(fw.left+25,fw.top+20)

# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기

w=pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive==False: # 현재 활성화가 되지 않았다면
    w.activate() # 활성화 (맨 앞으로 화면 가져오기)
    
pyautogui.sleep(1)

if w.isMaximized==False: # 현재 최대화가 되지 않았다면
    w.maximize() # 최대화

# if w.isMinimized==False: # 현재 최대화가 되지 않았다면
#     w.minimize() # 최대화
    
w.restore()  # 화면 원복

w.close() # 윈도우 닫기
"""
"""
import pyautogui

# 안녕하세요

# pyautogui.write("12345")
# pyautogui.write("Coding",interval=1)
#pyautogui.write("안녕")

#pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"],interval=1)
# t e s t 순서대로 적고 왼쪽 방향키 2번 오른쪽 방향키 2번 l a 순서대로 적고 enter 입력

# 특수 문자
# shift 4 -> $
# pyautogui.keyDown("shift") # shift 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyUp("shift") # shift 키를 뗀다


# # 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")
# pyautogui.keyUp("ctrl") # Ctrl + A

# # 간편한 조합키
# pyautogui.hotkey("ctrl","alt","shift","a")
# # Ctrl 누르고 > Alt 누르고 > Shift 누르고 > A 누르고 A 떼고 > Shift 떼고 > Alt 떼고
# pyautogui.hotkey("ctrl","a")

import pyperclip

# pyperclip.copy("안녕하세요") # "안녕하세요" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl","v") # 클립보드에 있는 내용을 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")
    
my_write("안녕하세요")

# 자동화 프로그램 종료
# win : ctrl + alt + del
"""
"""
import pyautogui

# print("곧 시작합니다...")
# pyautogui.countdown(3)
# print("자동화 시작")

# pyautogui.alert("자동화 수행에 실패하였습니다.","경고") # 확인 버튼만 있는 팝업
# result=pyautogui.confirm("계속 진행하시겠습니까?","확인")
# print(result)
# result=pyautogui.prompt("파일명을 무엇으로 하시겠습니까?","입력") # 사용자 입력
# print(result)
result=pyautogui.password("암호를 입력하세요") # 암호 입력
print(result)
"""
"""
#import logging

# logging.basicConfig(level=logging.DEBUG,format="%(asctime)s [%(levelname)s] %(message)s")

# # debug > info > warning > error > critical
# logging.debug("아 이거 누가 짠거야~~")
# logging.info("자동화 수행 준비")
# logging.warning("이 스크립트는 조금 오래 되었습니다. 실행상에 문제가 있을 수 있습니다.")
# logging.error("에러가 발생하였습니다. 에러 코드는 ...")
# logging.critical("복구가 불가능한 심각한 문제가 발생하였습니다...")

# 터미널과 파일에 함께 로그 남기기
import logging
from datetime import datetime

# 시간 [로그레벨] 메세지 형태로 로고를 작성
logFormatter=logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger=logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림 (터미널)
streamHandler=logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename=datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log") # mylogfile_20241212121212
fileHandler=logging.FileHandler(filename,encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logging.debug("로그를 남겨보는 테스트를 진행합니다.")
"""
"""
# 파일 기본
import os
# print(os.getcwd()) # current working directory 현재 작업 공간
# os.chdir("gui_basic") # gui_basic 으로 작업 공간 이동
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd())
# os.chdir("c:/") # 주어진 절대 경로로 이동
# print(os.getcwd())

# 파일 경로 만들기
# file_path=os.path.join(os.getcwd(),"my_file.txt") # 절대 경로 생성
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
#print(os.path.dirname(r"C:\Users\박찬우\Desktop\Python\__pycache__\my_file.txt"))

# 파일 정보 가져오기
# import time
# import datetime

# # 파일의 생성 날짜
# ctime=os.path.getctime("run_btn.png")
# print(ctime)
# # 날짜 정보를 strftime 을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime=os.path.getmtime("run_btn.png")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime=os.path.getatime("run_btn.png")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir("gui_basic")) # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기

# 파일 목록 가져오기 (하위 폴더 모두 포함)
# result=os.walk(".") # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
# print(result)

# for root,dirs,files in result:
#     print(root,dirs,files)

# 만약 폴더 내에서 특정 파일들을 찾으려면?
# name="desktop.py"
# result=[]
# for root,dirs,files in os.walk("."):
#     # [a.txt,b.txt,c.txt,desktop.py,...]
#     if name in files:
#         result.append(os.path.join(root,name))

# print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx, #.txt, 자동화*.png
# import fnmatch
# pattern="*.py" # .py 로 끝나는 모든 파일
# result=[]
# for root,dirs,files in os.walk("."):
#     # [a.txt,b.txt,c.txt,desktop.py,...]
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): # 이름과 패턴이 일치하면
#             result.append(os.path.join(root,name))
    
# print(result)

# 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir("gui_basic")) # gui_basic 은 폴더인가? True
# print(os.path.isfile("gui_basic")) # gui_basic 은 파일인가? False

# print(os.path.isdir("run_btn.png"))
# print(os.path.isfile("run_btn.png"))
 
# # 만약에 지정된 경로에 해당하는 파일 / 폴더가 없다면?
# print(os.path.isfile("run_butnnnn.png"))

# 주어진 경로가 존재하는지?
# if os.path.exists("run_btn.png"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")

# 파일 만들기
#open("new_file.txt","a").close() # 빈 파일 생성

# 파일명 변경하기
#os.rename("new_file.txt","new_file_rename.txt") # new_file.txt -> new_file_rename.txt 로 변경

# 파일 삭제하기
#os.remove("new_file_rename.txt")

# 폴더 만들기
#os.mkdir("new_folder") # 현재 경로 기준으로 파일 생성

#os.mkdir("new_folders/a/b/c") # 실패 : 하위 폴더를 가지는 폴더 생성 시도
#os.makedirs("new_folders/a/b/c") # 성공 : 하위 폴더를 가지는 폴더 생성 시도

# 폴더명 변경하기
#os.rename("new_folder","new_folder_rename")

# 폴더 지우기
#os.rmdir("new_folders") # 폴더 안이 비었을 때만 삭제 가능

import shutil # shell utilities

#shutil.rmtree("new_folders") # 폴더 안이 비어있지 않아도 삭제 가능
# 모든 파일이 삭제될 수 있으므로 주의

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("run_btn.png","test_folder") # 원본 파일 경로, 대상 폴더 경로
# 어떤 파일을 폴더 안에 새로운 이름으로 복사하기
# shutil.copy("run_btn.png","test_folder/copied_run_btn.png") # 원본 경로, 대상 경로(변경된 파일명까지)
# shutil.copyfile("run_btn.png","test_folder/copied_run_btn_2.png") # 원본 파일 경로, 대상 파일 경로

# shutil.copy2("run_btn.png","test_folder/copy2.png") # 원본 파일 경로, 대상 폴더(파일) 경로

# copy, copyfile : 메타정보 복사 X
# copy2 : 메타정보 복사 O

# 폴더 복사
# shutil.copytree("test_folder","test_folder2") # 원본 폴더 경로, 대상 폴더 경로
# shutil.copytree("test_folder","test_folder3")

# 폴더 이동
# shutil.move("test_folder","test_folder3")
# shutil.move("test_folder2","test_folder3")
# shutil.move("test_folder3","test_folder_rename") # 폴더명 변경되는 효과
"""
"""
import sys
import pyautogui
import pyperclip

pyautogui.hotkey("win","r") # 단축기 : win + r 입력
pyautogui.write("mspaint") # 프로그램 명 입력
pyautogui.press("enter") # 엔터 키 입력

# 그림판 나타날 때까지 2초 대기
pyautogui.sleep(2)

window=pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0] # 그림판 1개만 띄워져 있다고 가정
if window.isMaximized==False:
    window.maximize() # 최대화

# 글자 버튼 클릭
btn_text=pyautogui.locateOnScreen("btn_text.png",confidence=0.8)
if btn_text:
    pyautogui.click(btn_text,duration=0.5)
else:
    print("찾기 실패")
    sys.exit()

# 흰 영역 클릭
btn_brush=pyautogui.locateOnScreen("btn_brush.png")
pyautogui.click(btn_brush.left200,btn_brush.top+200)
def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")
    
my_write("참 잘했어요")

# 5초 대기
pyautogui.sleep(5)

# 프로그램 종료
window.close()
pyautogui.sleep(0.5)
pyautogui.press("n") # 저장하지 않음
"""