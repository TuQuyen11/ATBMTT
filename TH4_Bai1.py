from tkinter import *
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from Crypto.Cipher import PKCS1_v1_5
import base64

def hashing():
    content = text.get().encode()
    func = hashmode.get()

    if func == 0:
        result = MD5.new(content)
    if func == 1:
        result = SHA1.new(content)
    if func == 2:
        result = SHA256.new(content)
    if func == 3:
        result = SHA512.new(content)
    
    rs = result.hexdigest()
    texthash.delete(0,END)
    texthash.insert(INSERT,rs)

#Xây dựng giao diện
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

#Thêm các control
lb0 = Label(window, text=" ", font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

lb1 = Label(window, text="Chương trình Băm", font=("Arial Bold", 20))
lb1.grid(column=1, row=1)

plaintlb1 = Label(window, text="Văn bản", font=("Arial Bold", 13))
plaintlb1.grid(column=0, row=2)

text = Entry(window, width=100)
text.grid(column=1, row=2)

#Hàm băm
radioGroup = LabelFrame(window, text="Hàm băm")
radioGroup.grid(column=1, row=3)
hashmode = IntVar()
hashmode.set(-1)

md5_func = Radiobutton(radioGroup,
                       text="Hash MD5",
                       font=("Times New Roman", 11),
                       variable=hashmode,
                       value=0,
                       command=hashing
                       )
md5_func.grid(column=0, row=4)

sha1_func = Radiobutton(radioGroup,
                        text="Hash SHA1",
                        font=("Times New Roman", 11),
                        variable=hashmode,
                        value=1,
                        command=hashing
                        )
sha1_func.grid(column=0, row=5)

sha256_func = Radiobutton(radioGroup,
                       text="Hash SHA256",
                       font=("Times New Roman", 11),
                       variable=hashmode,
                       value=2,
                       command=hashing
                       )
sha256_func.grid(column=0, row=6)

sha512_func = Radiobutton(radioGroup,
                       text="Hash SHA512",
                       font=("Times New Roman", 11),
                       variable=hashmode,
                       value=3,
                       command=hashing
                       )
sha512_func.grid(column=0, row=7)

valuehash = Label(window, text="Giá trị Băm", font=("Arial Bold", 13))
valuehash.grid(column=0, row=8)
texthash = Entry(window, width=100)
texthash.grid(column=1, row=8)

#Hiển thị cửa sổ
window.geometry('800x600')
window.mainloop()
