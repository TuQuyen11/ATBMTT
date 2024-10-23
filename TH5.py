#Họ tên: Trần Tú Quyên
#MSSV: B2113317
#STT: 42

from tkinter import *
import tkinter as tk
from Crypto. PublicKey import RSA 
from Crypto import Random
from Crypto. Hash import SHA
from Crypto.Cipher import DES
from Crypto.Cipher import PKCS1_v1_5
import base64
from tkinter import filedialog

class MainWindow(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self)
        self.mahoa_Affine = Button(text="Mã hóa Affine",
                                   font=("Arial", 11),
                                   command=self.affine)
        self.mahoa_Affine.pack()

        self.mahoa_DES = Button(text="Mã hóa DES",
                                font=("Times New Roman",11),
                                command=self.des)
        self.mahoa_DES.pack()

        self.mahoa_RSA = Button(text="Mã hóa RSA",
                                font=("Arial", 11),
                                command=self.rsa)
        self.mahoa_RSA.pack()

        self.thoat=Button(text="Kết thúc",
                          font=("Times New Roman",11),
                          command=quit)
        self.thoat.pack()
        
    def affine(self):
        MAHOA_AFFINE(self)

    def des(self):
        MAHOA_DES(self)
    
    def rsa(self):
        MAHOA_RSA(self)

#CHƯƠNG TRÌNH DEMO AFFINE
class MAHOA_AFFINE(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Welcome to Demo AT&BMTT")
        self.geometry('800x600')

        self.lb1 = Label(self,
                         text="CHƯƠNG TRÌNH DEMO",
                         font=("Arial Bold", 20))
        self.lb1.grid(column=1, row=1)

        self.lb2 = Label(self,
                         text=" MẬT MÃ AFFINE",
                         font=("Arial Bold", 15))
        self.lb2.grid(column=0, row=2)

        self.lb3 = Label(self,
                         text="PLAIN TEXT",
                         font=("Arial", 15))
        self.lb3.grid(column=0, row=3)

        self.plaintxt = Entry(self, width=50)
        self.plaintxt.grid(column=1,row=3)

        self.lb4 = Label(self,
                         text="KEY PAIR",
                         font=("Arial", 15))
        self.lb4.grid(column=2, row=3)

        self.keya = Entry(self, width=5)
        self.keya.grid(column=3, row=3)

        self.keyb = Entry(self, width=5)
        self.keyb.grid(column=4, row=3)

        self.lb5 = Label(self,
                         text="CIPHER TEXT",
                         font=("Arial", 15))
        self.lb5.grid(column=0, row=4)

        self.ciphertxt = Entry(self, width=50)
        self.ciphertxt.grid(column=1, row=4)

        self.giaimatxt = Entry(self, width=50)
        self.giaimatxt.grid(column=3, row=4)

        #Button
        self.btn_mahoa = Button(self, 
                                text="Mã hóa",
                                command=self.mahoa_Affine)
        self.btn_mahoa.grid(column=5, row=3)

        self.btn_giaima = Button(self,
                                 text="Giải mã",
                                 command=self.giaima_Affine)
        self.btn_giaima.grid(column=2, row=4)

        self.btn_thoat = Button(self,
                                text="Quay về màn hình chính",
                                command=self.destroy)
        self.btn_thoat.grid(column=1, row=5)


    #Hàm mã hóa & Hàm giải mã
    def Char2Num(self, c):
        if c.isupper():
            return ord(c) - 65
        elif c.islower():
            return ord(c) - 97 + 26
        return -1
    
    def Num2Char(self, n):
        if 0 <= n < 26:
            return chr(n + 65)
        elif 26 <= n < 52:
            return chr(n - 26 + 97)
        return None
    
    def encryptAF(self, txt, a, b, m):
        r = ""
        for c in txt:
            if c == ' ':
                r += ' '
            else:
                e = (a * self.Char2Num(c) + b) % m
                r += self.Num2Char(e)
        return r
    
    def mahoa_Affine(self):
        a = int(self.keya.get())
        b = int(self.keyb.get())
        m = 52
        entxt = self.encryptAF(self.plaintxt.get(),a,b,m)
        self.ciphertxt.delete(0,END)
        self.ciphertxt.insert(INSERT,entxt)

    def xgcd(self, a, m):
        temp = m
        x0, x1, y0, y1 = 1, 0, 0, 1
        while m != 0:
            q, a, m = a // m, m, a % m
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
            if x0 < 0: 
                x0 += temp
        return x0
    
    def decryptAF(self, txt, a, b, m):
        r = ""
        a1 = self.xgcd(a, m)
        for c in txt:
            if c == ' ':
                r += ' '
            else:
                e = (a1 * (self.Char2Num(c) - b)) % m
                if e < 0:
                    e += m
                char = self.Num2Char(e)
                if char is not None:
                    r += char
                else:
                    r += '?' #không hợp lệ nên thêm ký tự ?
        return r

    def giaima_Affine(self):
        a = int(self.keya.get())
        b = int(self.keyb.get())
        m = 52
        entxt = self.decryptAF(self.ciphertxt.get(), a, b, m)
        self.giaimatxt.delete(0, END)
        self.giaimatxt.insert(INSERT, entxt)

#CHƯƠNG TRÌNH DEMO DES
def pad(s):
    #Thêm vào cuối số còn thiếu cho đủ bội của 8
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)
def unpad(s):
    return s[:-ord(s[len(s)-1:])]

class MAHOA_DES(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa đối xứng")
        self.geometry('800x600')
        
        self.lb1 = Label(self,
                         text="CHƯƠNG TRÌNH DEMO",
                         font=("Arial Bold", 20))
        self.lb1.grid(column=1, row=1)

        self.lb2 = Label(self,
                         text="MẬT MÃ ĐỐI XỨNG DES",
                         font=("Arial Bold", 15))
        self.lb2.grid(column=1, row=2)

        self.plainlb3 = Label(self,
                              text="Văn bản gốc",
                              font=("Arial", 14))
        self.plainlb3.grid(column=0, row=4)
        self.plaintxt = Entry(self, width=100)
        self.plaintxt.grid(column=1, row=4)

        self.plainlb4 = Label(self,
                              text="Khóa",
                              font=("Arial", 14))
        self.plainlb4.grid(column=0, row=5)
        self.keytxt = Entry(self, width=100)
        self.keytxt.grid(column=1, row=5)

        self.lb5 = Label(self,
                         text="Văn bản được mã hóa",
                         font=("Arial", 14))
        self.lb5.grid(column=0, row=6)
        self.ciphertxt = Entry(self, width=100)
        self.ciphertxt.grid(column=1, row=6)

        self.lb6 = Label(self,
                         text="Văn bản được giải mã",
                         font=("Arial", 14))
        self.lb6.grid(column=0, row=7)
        self.denctxt = Entry(self, width=100)
        self.denctxt.grid(column=1, row=7)

        #Button
        self.btn_enc = Button(self,
                              text="Mã hóa",
                              command=self.mahoa_DES)
        self.btn_enc.grid(column=1, row=9)

        self.btn_dec = Button(self,
                              text="Giải mã",
                              command=self.giaima_DES)
        self.btn_dec.grid(column=1, row=10)

        self.thoat = Button(self,
                            text="Quay về màn hình chính",
                            command=self.destroy)
        self.thoat.grid(column=1, row=11)
    
    #Hàm mã hóa & Hàm giải mã
    def mahoa_DES(self):
        txt = pad(self.plaintxt.get()).encode()
        key = pad(self.keytxt.get()).encode()
        cipher = DES.new(key, DES.MODE_ECB)
        entxt = cipher.encrypt(txt)
        entxt = base64.b64encode(entxt)
        self.ciphertxt.delete(0, END)
        self.ciphertxt.insert(INSERT, entxt)    

    def giaima_DES(self):
        txt = self.ciphertxt.get()
        txt = base64.b64decode(txt)
        key = pad(self.keytxt.get()).encode()
        cipher = DES.new(key, DES.MODE_ECB)
        detxt = unpad(cipher.decrypt(txt))
        self.denctxt.delete(0, END)
        self.denctxt.insert(INSERT,detxt)

#CHƯƠNG TRÌNH DEMO RSA
class MAHOA_RSA(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")
        self.geometry('800x600')

        self.lb1 = Label(self,
                            text="CHƯƠNG TRÌNH DEMO",
                            font=("Arial", 20))
        self.lb1.grid(column=1,row=1)

        self.lb2 = Label(self,
                            text="MẬT MÃ ĐỐI XỨNG RSA",
                            font=("Arial", 15))
        self.lb2.grid(column=1,row=2)

        self.lb3 = Label(self,
                            text="Văn bản gốc",
                            font=("Arial", 15))
        self.lb3.grid(column=0,row=3)

        self.plaintxt = Entry(self,width=100)
        self.plaintxt.grid(column=1,row=3)

        self.lb4 = Label(self,
                            text="Văn bản được mã hóa",
                            font=("Arial", 15))
        self.lb4.grid(column=0,row=4)

        self.vb_mahoa = Entry(self,width=100)
        self.vb_mahoa.grid(column=1,row=4)

        self.lb5 = Label(self,
                            text="Văn bản được giải mã",
                            font=("Arial", 15))
        self.lb5.grid(column=0,row=5)

        self.vb_giaima = Entry(self,width=100)
        self.vb_giaima.grid(column=1,row=5)

        self.lb6 = Label(self,
                            text="Khóa cá nhân",
                            font=("Arial", 15))
        self.lb6.grid(column=0,row=6)

        self.pri_key = Entry(self,width=100)
        self.pri_key.grid(column=1,row=6)

        self.lb7 = Label(self,
                            text="Khóa công khai",
                            font=("Arial", 15))
        self.lb7.grid(column=0,row=7)

        self.pub_key = Entry(self,width=100)
        self.pub_key.grid(column=1,row=7)

        #Button
        self.tao_khoa = Button(self,
                                text="Tạo khóa",
                                command=self.generate_key)
        self.tao_khoa.grid(column=1,row=8)
        self.mahoa = Button(self,
                            text="Mã hóa",
                            command=self.ma_hoa_rsa)
        self.mahoa.grid(column=1,row=9)
        self.giaima = Button(self,
                                text="Giải mã",
                                command=self.giai_ma_rsa)
        self.giaima.grid(column=1,row=10)
        self.openfile = Button(self,
                                text="Mở file plaintext"
                                )
        self.openfile.grid(column=1,row=11)
        self.thoat = Button(self,
                            text="Quay về màn hình chính",
                            command=self.destroy)
        self.thoat.grid(column=1,row=12)       
                
    #Tạo Khóa
    def generate_key(self):
        key = RSA.generate (1024)

        pri = self.save_file(key.exportKey('PEM'),'wb','Lưu khóa cá nhân',
        (("All files", "*.*"), ("PEM files", "*.pem")), ".pem")
                                
        pub = self.save_file (key.publickey ().exportKey('PEM'), 'wb','Lưu khóa công khai',
        (("All files", "*.*"), ("PEM files", "*.pem")), ".pem")

        self.pri_key.delete(0, END)
        self.pri_key.insert (END, key.exportKey('PEM'))
        self.pub_key.delete(0, END)
        self.pub_key.insert(END, key.publickey().exportKey('PEM'))
    #Cài đặt thủ tục save_file
    def save_file(self,content,_mode,_title,_filetypes,_defaultextension):
        f = filedialog.asksaveasfile(mode = _mode,
                                    initialdir= "C:/",
                                    title=_title,
                                    filetypes=_filetypes,
                                    defaultextension=_defaultextension)
        if f is None: return
        f.write(content)
        f.close()
    #Mã Hóa
    def get_key (self,key_style):
        filename = filedialog.askopenfilename (initialdir = "C:/", 
                                            title = "Open " + key_style,
                                                filetypes = (("PEM files", "*.pem"), ("All files", "*.*")))
        if filename is None: return
        file = open(filename, "rb")
        key = file.read()
        file.close()
        return RSA. importKey (key)

    def ma_hoa_rsa (self):
        txt = self.plaintxt.get().encode()
        pub_key = self.get_key("Public Key") 
        cipher = PKCS1_v1_5.new (pub_key)
        entxt = cipher.encrypt (txt)
        entxt = base64.b64encode (entxt)

        self.vb_mahoa.delete(0, END)
        self.vb_mahoa.insert (INSERT, entxt)

    def giai_ma_rsa(self):
        entxt = self.vb_mahoa.get().encode()
        pri_key = self.get_key("Private Key") 
        cipher = PKCS1_v1_5.new(pri_key)
        entxt = base64.b64decode(entxt)  # Giải mã base64
        plaintxt_decoded = cipher.decrypt(entxt, None)

        self.vb_giaima.delete(0, END)
        self.vb_giaima.insert (INSERT, plaintxt_decoded)


    

def main():
    window = tk.Tk()
    window.title("Chương trình chính")
    window.geometry('300x200')
    MainWindow(window)
    window.mainloop()
main()