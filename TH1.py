# -*- coding: utf8 -*-
from tkinter import *
#Khởi tạo màn hình chính
window = Tk()
window.title("Welcome to Demo AT&BMTT")

#Xây dựng giao diện
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

lbl = Label(window, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

lb2 = Label(window, text="MẬT MÃ AFFINE",font=("Arial Bold", 15))
lb2.grid(column=0, row=2)

plainlb3 = Label(window, text="PLAIN TEXT",font=("Arial", 14))
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window,width=20)
plaintxt.grid(column=1, row=3)

KEYlb4 = Label(window, text="KEY PAIR",font=("Arial", 14))
KEYlb4.grid(column=2, row=3)
KEYA1 = Entry(window,width=3)
KEYA1.grid(column=3, row=3)
KEYB1 = Entry(window,width=5)
KEYB1.grid(column=4, row=3)

plainlb4 = Label(window,text="CIPHER TEXT",font=("Arial", 14))
plainlb4.grid(column=0,row=4)
plaintxt1= Entry(window,width=20)
plaintxt1.grid(column=1,row=4)

plaintxt2= Entry(window,width=20)
plaintxt2.grid(column=3,row=4)

#Cài đặt các thủ tục
#Chuyển ký tự thành số
def Char2Num(c):
    if c.isupper():
        return ord(c) - 65
    elif c.islower():
        return ord(c) - 97 + 26
    return -1

#Chuyển số thành ký tự
def Num2Char(n):
    if 0 <= n < 26:
        return chr(n + 65)
    elif 26 <= n < 52:
        return chr(n - 26 + 97)
    return None

#Mã hóa
def encryptAF(txt, a, b, m):
    r = ""
    for c in txt:
        if c == ' ':
            r += ' '
        else:
            e = (a * Char2Num(c) + b) % m
            r += Num2Char(e)
    return r

def mahoa():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 52
    entxt = encryptAF(plaintxt.get(),a,b,m)

    plaintxt1.delete(0,END)
    plaintxt1.insert(INSERT,entxt)

#Giải mã
def xgcd(a, m):
    temp = m
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while m != 0:
        q, a, m = a // m, m, a % m
        x0 = x1
        x1 = x0 - q * x1
        y0 = y1 
        y1 = y0 - q * y1
        if x0 < 0:
            x0 = temp+x0
    return x0

def decryptAF(txt, a, b, m):
    r = ""
    a1 = xgcd(a, m)
    for c in txt:
        if c == ' ':
            r += ' '
        else:
            e = (a1 * (Char2Num(c) - b)) % m
            if e < 0:
                e += m
            char = Num2Char(e)
            if char is not None:
                r += char
            else:
                r += '?' #không hợp lệ nên thêm ký tự ?
    return r

def giaima():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 52
    entxt = decryptAF(plaintxt1.get(), a, b, m)
    
    plaintxt2.delete(0, END)
    plaintxt2.insert(INSERT, entxt)

#Tạo nút Button
AFbtn = Button(window, text="Mã Hóa",command=mahoa)
AFbtn.grid(column=5, row=3)

DEAFbtn = AFbtn = Button(window, text="Giai Ma",command=giaima)
AFbtn.grid(column=2, row=4)

#Hiển thị
window.geometry('800x200')
window.mainloop()
