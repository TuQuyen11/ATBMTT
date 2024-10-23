from Crypto. PublicKey import RSA 
from Crypto import Random
from Crypto. Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64
from tkinter import filedialog
from tkinter import *

#Xây dựng giao diện
window = Tk()
window.title("Welcome to Demo An toàn bảo mật thông tin")

#Thêm các control
lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lb1 = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lb1.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ ĐỐI XỨNG RSA", font=("Arial Bold", 15))
lb2.grid(column=1, row=2)

plainlb1 = Label(window, text="Văn bản gốc", font=("Arial Bold", 13))
plainlb1.grid(column=0, row=3)
plaintxt = Entry(window, width=100)
plaintxt.grid(column=1, row=3)

plainlb2 = Label(window, text="Văn bản được mã hóa", font=("Arial Bold", 13))
plainlb2.grid(column=0, row=4)
ciphertxt = Entry (window, width=100)
ciphertxt.grid(column=1, row=4)

plainlb3 = Label(window, text="Văn bản được giải mã", font=("Arial Bold", 13))
plainlb3.grid(column=0, row=5)
denctxt = Entry(window, width=100)
denctxt.grid(column=1, row=5)

plainlb4 = Label(window, text="Khóa cá nhân", font=("Arial Bold", 13))
plainlb4.grid(column=0, row=6)
pri_key = Entry(window, width=100)
pri_key.grid(column=1, row=6)

plainlb4 = Label(window, text="Khóa công khai", font=("Arial Bold", 13))
plainlb4.grid(column=0, row=7)
pub_key = Entry(window, width=100)
pub_key.grid(column=1, row=7)

#Tạo Khóa
def generate_key():
    key = RSA.generate (1024)

    pri = save_file(key.exportKey('PEM'),'wb','Lưu khóa cá nhân',
    (("All files", "*.*"), ("PEM files", "*.pem")), ".pem")
                            
    pub = save_file (key.publickey ().exportKey('PEM'), 'wb','Lưu khóa công khai',
    (("All files", "*.*"), ("PEM files", "*.pem")), ".pem")

    pri_key.delete(0, END)
    pri_key.insert (END, key.exportKey('PEM'))
    pub_key.delete(0, END)
    pub_key.insert(END, key.publickey().exportKey('PEM'))

#Cài đặt thủ tục save_file
def save_file(content,_mode,_title,_filetypes,_defaultextension):
    f = filedialog.asksaveasfile(mode = _mode,
                                initialdir= "C:/",
                                title=_title,
                                filetypes=_filetypes,
                                defaultextension=_defaultextension)
    if f is None: return
    f.write(content)
    f.close()


#Mã Hóa
def get_key (key_style):
    filename = filedialog.askopenfilename (initialdir = "C:/", 
                                           title = "Open " + key_style,
                                            filetypes = (("PEM files", "*.pem"), ("All files", "*.*")))
    if filename is None: return
    file = open(filename, "rb")
    key = file.read()
    file.close()
    return RSA. importKey (key)

def ma_hoa_rsa ():
    txt = plaintxt.get().encode()
    pub_key = get_key("Public Key") 
    cipher = PKCS1_v1_5.new (pub_key)
    entxt = cipher.encrypt (txt)
    entxt = base64.b64encode (entxt)

    ciphertxt.delete(0, END)
    ciphertxt.insert (INSERT, entxt)

def giai_ma_rsa():
    entxt = ciphertxt.get().encode()
    pri_key = get_key("Private Key") 
    cipher = PKCS1_v1_5.new(pri_key)
    entxt = base64.b64decode(entxt)  # Giải mã base64
    plaintxt_decoded = cipher.decrypt(entxt, None)

    denctxt.delete(0, END)
    denctxt.insert (INSERT, plaintxt_decoded)

#Tạo nút có tên AFbtn
AFbtn = Button(window, text="Tạo khóa", command=generate_key)
AFbtn.grid(column=1, row=8)
AFbtn = Button(window, text="Mã hóa", command=ma_hoa_rsa)
AFbtn.grid(column=1, row=9)
AFbtn1 = Button(window, text="Giải mã", command=giai_ma_rsa)
AFbtn1.grid(column=1, row=10)

#Hiển thị cửa sổ
window.geometry('800x600')
window.mainloop()


    


