
from Crypto.Cipher import DES
import base64
from tkinter import *

#Xây dựng giao diện
window = Tk()
window.title("Welcome to Demo AT&BMTT")

def pad (s):
#Thêm vào cuối số còn thiếu cho đủ bội của 8
    return s + (8 - len(s )% 8) * chr (8 - len(s) % 8)
def unpad (s):
    return s[:-ord (s[len(s)-1:])]
#Mã hóa
def mahoa_DES():
    txt = pad(plaintxt.get()).encode("utf8")
    key = pad (keytxt.get()).encode("utf8")
    cipher = DES.new (key, DES.MODE_ECB)
    entxt = cipher.encrypt (txt)
    entxt = base64.b64encode (entxt)
    ciphertxt.delete(0,END)
    ciphertxt.insert (INSERT,entxt)
#Giải mã
def giaima_DES () :
    txt = ciphertxt.get()
    txt = base64.b64decode(txt)
    key = pad (keytxt.get()).encode("utf8") 
    cipher = DES.new(key, DES.MODE_ECB) 
    detxt = unpad (cipher.decrypt (txt))
    denctxt.delete(0,END) 
    denctxt.insert (INSERT, detxt)

#Thêm các control
lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lb1 = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lb1.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ ĐỐI XỨNG DES", font=("Arial Bold", 15))
lb2.grid(column=1, row=2)

plainlb1 = Label(window, text="Văn bản gốc", font=("Arial Bold", 13))
plainlb1.grid(column=0, row=3)
plaintxt = Entry(window, width=100)
plaintxt.grid(column=1, row=3)

plainlb2 = Label(window, text="Khóa", font=("Arial Bold", 13))
plainlb2.grid(column=0, row=4)
keytxt = Entry(window, width=100)
keytxt.grid(column=1, row=4)

plainlb3 = Label(window, text="Văn bản được mã hóa", font=("Arial Bold", 13))
plainlb3.grid(column=0, row=5)
ciphertxt = Entry (window, width=100)
ciphertxt.grid(column=1, row=5)

plainlb4 = Label(window, text="Văn bản được giải mã", font=("Arial Bold", 13))
plainlb4.grid(column=0, row=6)
denctxt = Entry(window, width=100)
denctxt.grid(column=1, row=6)

#Tạo nút có tên AFbtn
AFbtn = Button(window, text="Mã hóa", command=mahoa_DES)
AFbtn.grid(column=1, row=7)
AFbtn1 = Button(window, text="Giải mã", command=giaima_DES)
AFbtn1.grid(column=1, row=8)

#Hiển thị cửa sổ
window.geometry('800x600')
window.mainloop()
