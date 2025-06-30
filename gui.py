# -*- coding: utf-8 -*-
"""
from tkinter import *

root=Tk()
root.title("원하는 이름")
root.geometry("640x480+300+100") # 가로 x 세로 + x 좌표 + y 좌표

root.resizable(False,False) # x , y 값 변경 불가 (창 크기 변경 불가)


root.mainloop()
"""
"""
from tkinter import *

root=Tk()
root.title("GUI")

btn1=Button(root,text="버튼1")
btn1.pack()

# padx pady 는 text 길이에 의해 버튼의 크기가 커질 수 있음
btn2=Button(root,padx=5,pady=10,text="버튼2") 
btn2.pack()

btn3=Button(root,padx=10,pady=5,text="버튼3")
btn3.pack()

# padx pady 와 달리 width height 는 text 값에 상관없이 버튼 크기 고정
btn4=Button(root,width=10,height=3,text="버튼4")
btn4.pack()

btn5=Button(root,fg="red",bg="yellow",text="버튼5")
btn5.pack()

photo=PhotoImage(file="gui_basic/img.png")
btn6=Button(root,image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7=Button(root,text="동작하는 버튼",command=btncmd)
btn7.pack()

root.mainloop()
"""
"""
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("640x480")

label1=Label(root,text="안녕하세요")
label1.pack()

photo=PhotoImage(file="gui_basic/img.png")
label2=Label(root,image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")
    
    global photo2
    photo2=PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)
    
btn=Button(root,text="클릭",command=change)
btn.pack()

root.mainloop()
"""
"""
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("640x480")

txt=Text(root,width=30,height=5)
txt.pack()
txt.insert(END,"글자를 입력하세요")

e=Entry(root,width=30)
e.pack()
e.insert(0,"한 줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0",END)) # 1 : 첫 번째 라인 0 : 0번째 컬럼 위치
    print(e.get())
    # 내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)
    
    

btn=Button(root,text="클릭",command=btncmd)
btn.pack()

root.mainloop()
"""
"""
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("640x480")

listbox=Listbox(root,selectmode="extended",height=0)
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()

def btncmd():
    # 삭제
    #listbox.delete(0) 
    
    # 갯수 확인
    #print("리스트에는",listbox.size(),"개가 있어요")
    
    # 항목 확인 (시작 idx, 끝 idx)
    #print("1번째부터 3번째까지의 항목 : ",listbox.get(0,2))
    
    # 선택된 항목 확인 (위치로 반환 ex) (1,2,3))
    print("선택된 항목 : ",listbox.curselection())
    

btn=Button(root,text="클릭",command=btncmd)
btn.pack()

root.mainloop()
"""
"""
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("640x480")

chkvar=IntVar() # chkvar에 int 형으로 값을 저장한다
chkbox=Checkbutton(root,text="오늘 하루 보지 않기",variable=chkvar)
#chkbox.select() # 자동 선택 처리
#chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2=IntVar()
chkbox2=Checkbutton(root,text="일주일동안 보지 않기",variable=chkvar2)
chkbox2.pack()



def btncmd():
    print(chkvar.get()) # 0: 체크 해제 1: 체크
    print(chkvar2.get())
    

btn=Button(root,text="클릭",command=btncmd)
btn.pack()

root.mainloop()
"""
"""
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("640x480")

Label(root,text="메뉴를 선택하세요").pack()

burger_var=IntVar() # 여기에 int 형으로 값을 저장
btn_burger1=Radiobutton(root,text="햄버거",value=1,variable=burger_var)
btn_burger1.select() # 기본 값 선택
btn_burger2=Radiobutton(root,text="치즈버거",value=2,variable=burger_var)
btn_burger3=Radiobutton(root,text="치킨버거",value=3,variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root,text="음료를 선택하세요").pack()


drink_var=StringVar()
btn_drink1=Radiobutton(root,text="콜라",value="콜라",variable=drink_var)
btn_drink1.select() # 기본 값 선택
btn_drink2=Radiobutton(root,text="사이다",value="사이다",variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get()) # 음료 중 선택된 값을 출력
    
btn=Button(root,text="주문",command=btncmd)
btn.pack()

root.mainloop()
"""
"""
import tkinter.ttk as ttk
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("640x480")

values=[str(i) + "일" for i in range(1,32)] # 1~31 까지의 숫자
combobox=ttk.Combobox(root,height=5,values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox=ttk.Combobox(root,height=5,values=values,state="readonly")
readonly_combobox.current(0) # 0 번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택한 값 표시
    print(readonly_combobox.get())
    
btn=Button(root,text="선택",command=btncmd)
btn.pack()

root.mainloop()
"""
"""
import time
import tkinter.ttk as ttk
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("640x480")

#progressbar=ttk.Progressbar(root,maximum=100,mode="indeterminate")
progressbar=ttk.Progressbar(root,maximum=100,mode="determinate")

progressbar.start(10) # 10 ms 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop() # 작동 중지
    
btn=Button(root,text="중지",command=btncmd)
btn.pack()
########################################################
p_var2=DoubleVar()
progressbar2=ttk.Progressbar(root,maximum=100,length=150,variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1,101): # 1 ~ 100
        time.sleep(0.01) # 0.01 초 대기
        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn=Button(root,text="시작",command=btncmd2)
btn.pack()

root.mainloop()
"""
"""
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("640x480")

def create_new_file():
    print("새 파일을 만듭니다")

menu=Menu(root)

menu_file=Menu(menu,tearoff=0)
menu_file.add_command(label="New File",command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File....")
menu_file.add_separator()
menu_file.add_command(label="Save All",state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit",command=root.quit)
menu.add_cascade(label="File",menu=menu_file)

# Edit 메뉴 (빈 값)
menu.add_cascade(label="Exit")

# Language 메뉴 추가 (radio 버튼을 통해서 추가)
menu_lang=Menu(menu,tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language",menu=menu_lang)

# View 메뉴
menu_view=Menu(menu,tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View",menu=menu_view)

root.config(menu=menu)
root.mainloop()
"""
"""
import tkinter.messagebox as msgbox
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("640x480")

# 기차 예매 시스템
def info():
    msgbox.showinfo("알림","정상적으로 예매 완료되었습니다.")
def warn():
    msgbox.showwarning("경고","해당 좌석은 매진되었습니다.")
def error():
    msgbox.showerror("에러","결제 오류가 발생하였습니다.")
def okcancel():
    msgbox.askokcancel("확인 / 취소","해당 좌석은 유아동반석입니다. 예매하시겠습니까?")
def retrycancel():
    msgbox.askretrycancel("재시도 / 취소","일시적인 오류입니다. 다시 시도하시겠습니까?")
def yesno():
    msgbox.askyesno("예 / 아니오","해당 좌석은 역방향입니다. 예매하시겠습니까?")
def yesnocancel():
    response=msgbox.askyesnocancel(title=None,message="예매 내역이 저장되지 않았습니다. \n저장 후 프로그램을 종료하시겠습니까?")
    # 네 : 저장 후 종료 
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업하겠음)
    print("응답 : ",response)
    if response==1: # 네
        print("예")
    elif response==0: # 아니오
        print("아니오")
    else:
        print("취소")
    
    
Button(root,command=info,text="알림").pack()
Button(root,command=warn,text="경고").pack()
Button(root,command=error,text="에러").pack()

Button(root,command=okcancel,text="확인 취소").pack()
Button(root,command=retrycancel,text="재시도 취소").pack()
Button(root,command=yesno,text="예 아니오").pack()
Button(root,command=yesnocancel,text="예 아니오 취소").pack()


root.mainloop()
"""
"""
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("640x480")

Label(root,text="메뉴를 선택해 주세요").pack(side="top")

Button(root,text="주문하기").pack(side="bottom")


# 메뉴 프레임
frame_burger=Frame(root,relief="solid",bd=1)
frame_burger.pack(side="left",fill="both",expand=True)

Button(frame_burger,text="햄버거").pack()
Button(frame_burger,text="치즈버거").pack()
Button(frame_burger,text="치킨버거").pack()

# 음료 프레임
frame_drink=LabelFrame(root,text="음료")
frame_drink.pack(side="right",fill="both",expand=True)

Button(frame_drink,text="콜라").pack()
Button(frame_drink,text="사이다").pack()

root.mainloop()
"""
"""
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("640x480")

frame=Frame(root)
frame.pack()

scrollbar=Scrollbar(frame)
scrollbar.pack(side="right",fill="y")

# set 이 없으면 스크롤을 내려도 다시 올라옴
listbox=Listbox(frame,selectmode="extended",height=10,yscrollcommand=scrollbar.set)
for i in range(1,32): # 1~31
    listbox.insert(END,str(i)+"일") # 1일 , 2일 ....
    
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)    

root.mainloop()
"""
"""
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("640x480")

# 맨 윗줄
btn_f16=Button(root,text="F16",width=5,height=2)
btn_f17=Button(root,text="F17",width=5,height=2)
btn_f18=Button(root,text="F18",width=5,height=2)
btn_f19=Button(root,text="F19",width=5,height=2)

btn_f16.grid(row=0,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_f17.grid(row=0,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_f18.grid(row=0,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_f19.grid(row=0,column=3,sticky=N+E+W+S,padx=3,pady=3)

# clear 줄
btn_clear=Button(root,text="clear",width=5,height=2)
btn_equal=Button(root,text="=",width=5,height=2)
btn_div=Button(root,text="/",width=5,height=2)
btn_mul=Button(root,text="*",width=5,height=2)

btn_clear.grid(row=1,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_equal.grid(row=1,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_div.grid(row=1,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_mul.grid(row=1,column=3,sticky=N+E+W+S,padx=3,pady=3)

# 7 시작 줄
btn_7=Button(root,text="7",width=5,height=2)
btn_8=Button(root,text="8",width=5,height=2)
btn_9=Button(root,text="9",width=5,height=2)
btn_sub=Button(root,text="-",width=5,height=2)

btn_7.grid(row=2,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_8.grid(row=2,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_9.grid(row=2,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_sub.grid(row=2,column=3,sticky=N+E+W+S,padx=3,pady=3)

# 4 시작 줄
btn_4=Button(root,text="4",width=5,height=2)
btn_5=Button(root,text="5",width=5,height=2)
btn_6=Button(root,text="6",width=5,height=2)
btn_add=Button(root,text="+",width=5,height=2)

btn_4.grid(row=3,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_5.grid(row=3,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_6.grid(row=3,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_add.grid(row=3,column=3,sticky=N+E+W+S,padx=3,pady=3)

# 1 시작 줄
btn_1=Button(root,text="1",width=5,height=2)
btn_2=Button(root,text="2",width=5,height=2)
btn_3=Button(root,text="3",width=5,height=2)
btn_enter=Button(root,text="enter",width=5,height=2) # 세로로 합쳐짐

btn_1.grid(row=4,column=0,sticky=N+E+W+S,padx=3,pady=3)
btn_2.grid(row=4,column=1,sticky=N+E+W+S,padx=3,pady=3)
btn_3.grid(row=4,column=2,sticky=N+E+W+S,padx=3,pady=3)
btn_enter.grid(row=4,column=3,rowspan=2,sticky=N+E+W+S,padx=3,pady=3) # 현재 위치로부터 아래쪽으로 합쳐짐

# 0 시작 줄
btn_0=Button(root,text="0",width=5,height=2) # 가로로 합쳐짐
btn_point=Button(root,text=".",width=5,height=2)

btn_0.grid(row=5,column=0,columnspan=2,sticky=N+E+W+S,padx=3,pady=3)
btn_point.grid(row=5,column=2,sticky=N+E+W+S,padx=3,pady=3)

root.mainloop()
"""
"""
import os
from tkinter import *

root=Tk()
root.title("제목 없음 - Window 메모장")
root.geometry("640x480")

# 열기, 저장 파일 이름
filename="mynote.txt"

def open_file():
    if os.path.isfile(filename): # 파일 있으면 True, 없으면 False
        with open(filename,"r",encoding="utf8") as file:
            txt.delete("1.0",END) # 텍스트 위젯 본문 삭제
            txt.insert(END,file.read()) # 파일 내용을 본문에 입력

def save_file():
    with open(filename,"w",encoding="utf8") as file:
        file.write(txt.get("1.0",END)) # 모든 내용을 가져와서 저장
        
menu=Menu(root)

menu_file=Menu(menu,tearoff=0)
menu_file.add_command(label="열기",command=open_file)
menu_file.add_command(label="저장",command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기",command=root.quit)
menu.add_cascade(label="파일",menu=menu_file)

# 편집, 서식, 보기, 도움말
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤 바
scrollbar=Scrollbar(root)
scrollbar.pack(side="right",fill="y")

# 본문 영역
txt=Text(root,yscrollcommand=scrollbar.set)
txt.pack(side="left",fill="both",expand=True)

scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()
"""

import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # __all__
from tkinter import filedialog
from PIL import Image

root=Tk()
root.title("Photo Plus")

# 파일 추가
def add_file():
    files=filedialog.askopenfilenames(title="이미지 파일을 선택하세요",\
    filetypes=(("PNG 파일","*.png"),("모든파일","*.*")),\
    initialdir=r"C:\Users\박찬우\Desktop\Python\__pycache__\image")
    # 최초의 사용자가 지정한 경로를 보여줌
    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END,file)
# 선택 삭제
def del_file():
    print(list_file.curselection())

    for index in reversed(list_file.curselection()):
        list_file.delete(index)
        
# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected=filedialog.askdirectory()
    if folder_selected=="": # 사용자가 취소를 누를 때
        return
    txt_dest_path.delete(0,END)
    txt_dest_path.insert(0,folder_selected)

# 이미지 통합
def merge_image():
    try:
        # 가로넓이
        img_width=cmb_width.get()
        if img_width=="원본유지":
            img_width=-1 # -1 일때는 원본 기준으로
        else:
            img_width=int(img_width)
            
        # 간격
        img_space=cmb_space.get()
        if img_space=="좁게":
            img_space=30
        elif img_space=="보통":
            img_space=60
        elif img_space=="넓게":
            img_space=90
        else: # 없음
            img_space=0
    
        # 포멧
        img_format=cmb_format.get().lower() # PNG,JPG,BMP 값을 받아와서 소문자로 변경
    
    
        images=[Image.open(x) for x in list_file.get(0,END)]
        
        # 이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes=[] # [(width1,height1),(width2,height2),....]
        if img_width>-1:
            # width 값 변경
            image_sizes=[(int(img_width),int(img_width*x.size[1]/x.size[0])) for x in images]
        else:
            # 원본 사이즈 사용
            image_sizes=[(x.size[0],x.size[1])for x in images]
            
        
        widths,heights=zip(*(image_sizes))
        
        # 최대 넓이 ,전체 높이 구해옴
        max_width,total_height=max(widths),sum(heights)
        
        # 스케치북 준비
        if img_space>0: # 이미지 간격 옵션 적용
            total_height+=(img_space*(len(images)-1))
        result_img=Image.new("RGB",(max_width,total_height),(255,255,255)) # 배경 흰색
        y_offset=0 # y 위치
            
        for idx,img in enumerate(images):
            # width 가 원본유지가 아닐 때에는 이미지 크기 조정
            if img_width>-1:
                img=img.resize(image_sizes[idx])
                
                
            result_img.paste(img,(0,y_offset))
            y_offset+=(img.size[1]+img_space) # height 값 + 사용자가 지정한 간격
            
            progress=(idx+1)/len(images)*100 # 실제 percent 정보를 계산
            p_var.set(progress)
            progress_bar.update()
        
        # 포멧 옵션 처리
        file_name="photo"+img_format
        dest_path=os.path.join(txt_dest_path.get(),file_name)
        result_img.save(dest_path)
        msgbox.showinfo("알림","작업이 완료되었습니다.")
    except Exception as err:
        msgbox.showerror("에러",err)
# 시작
def start():
    # 각 옵션들 값을 확인
    
    # 파일 목록 확인
    if list_file.size()==0:
        msgbox.showwarning("경고","이미지 파일을 추가하세요")
        return
    
    # 저장 경로 확인
    if len(txt_dest_path.get())==0:
        msgbox.showwarning("경고","저장 경로를 선택하세요")
        return
    
    # 이미지 통합 작업
    merge_image()

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame=Frame(root)
file_frame.pack(fill="x",padx=5,pady=5) # 간격 띄우기

btn_add_file=Button(file_frame,padx=5,pady=5,width=12,text="파일추가",command=add_file)
btn_add_file.pack(side="left")

btn_del_file=Button(file_frame,padx=5,pady=5,width=12,text="선택삭제",command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame=Frame(root)
list_frame.pack(fill="both",padx=5,pady=5)

scrollbar=Scrollbar(list_frame)
scrollbar.pack(side="right",fill="y")

list_file=Listbox(list_frame,selectmode="extended",height=15,yscrollcommand=scrollbar.set)
list_file.pack(side="left",fill="both",expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame=LabelFrame(root,text="저장경로")
path_frame.pack(fill="x",padx=5,pady=5,ipady=5)

txt_dest_path=Entry(path_frame) 
txt_dest_path.pack(side="left",fill="x",expand=True,padx=5,pady=5,ipady=4) # 높이 변경

btn_dest_path=Button(path_frame,text="찾아보기",width=10,command=browse_dest_path)
btn_dest_path.pack(side="right",padx=5,pady=5)

# 옵션 프레임
frame_option=LabelFrame(root,text="옵션")
frame_option.pack(padx=5,pady=5,ipady=5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width=Label(frame_option,text="가로 넓이",width=8)
lbl_width.pack(side="left",padx=5,pady=5)

# 가로 넓이 콤보
opt_width=["원본유지","1024","800","640"]
cmb_width=ttk.Combobox(frame_option,state="readonly",values=opt_width,width=10)
cmb_width.current(0)
cmb_width.pack(side="left",padx=5,pady=5)

# 2. 간격 옵션
# 간격 옵션 레이블 
lbl_space=Label(frame_option,text="간격",width=8)
lbl_space.pack(side="left",padx=5,pady=5)

# 간격 옵션 콤보
opt_space=["없음","좁게","보통","넓게"]
cmb_space=ttk.Combobox(frame_option,state="readonly",values=opt_space,width=10)
cmb_space.current(0)
cmb_space.pack(side="left",padx=5,pady=5)

# 3. 파일 포멧 옵션
# 파일 포멧 레이블 
lbl_format=Label(frame_option,text="간격",width=8)
lbl_format.pack(side="left",padx=5,pady=5)

# 파일 포멧 콤보
opt_format=["PNG","JPG","BMP"]
cmb_format=ttk.Combobox(frame_option,state="readonly",values=opt_format,width=10)
cmb_format.current(0)
cmb_format.pack(side="left",padx=5,pady=5)

# 진행 상황 Progress Bar
frame_progress=LabelFrame(root,text="진행상황")
frame_progress.pack(fill="x",padx=5,pady=5,ipady=5)

p_var=DoubleVar()
progress_bar=ttk.Progressbar(frame_progress,maximum=100,variable=p_var)
progress_bar.pack(fill="x",padx=5,pady=5)

# 실행 프레임
frame_run=Frame(root)
frame_run.pack(fill="x",padx=5,pady=5)

btn_close=Button(frame_run,padx=5,text="닫기",width=12,command=root.quit)
btn_close.pack(side="right",padx=5,pady=5)

btn_start=Button(frame_run,padx=5,text="시작",width=12,command=start)
btn_start.pack(side="right",padx=5,pady=5)

root.resizable(False,False)
root.mainloop()

























































