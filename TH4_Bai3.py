from tkinter import *
import os
import hashlib
import random

# Xây dựng giao diện
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

# Cài đặt các Control
lb = Label(window, text="Đăng nhập", font=("Arial Bold", 20))
lb.grid(column=1, row=0)

lb1 = Label(window, text="Tên đăng nhập", font=("Arial Bold", 15))
lb1.grid(column=0, row=1)
username = Entry(window, width=100)
username.grid(column=1, row=1)

lb2 = Label(window, text="Mật khẩu", font=("Arial Bold", 15))
lb2.grid(column=0, row=2)
password = Entry(window, show="*", width=100)  # Ẩn mật khẩu
password.grid(column=1, row=2)

# Hàm mã hóa mật khẩu bằng các thuật toán khác nhau
def hash_password(password, algorithm):
    hash_object = getattr(hashlib, algorithm)(password.encode('utf-8'))
    return hash_object.hexdigest()

# Hàm kiểm tra tài khoản trong file
def check_account(username, password):
    filename = 'CSDL.csv'
    
    if os.path.exists(filename):
        with open(filename, mode='r', newline='') as file:
            next(file)  # Bỏ qua dòng tiêu đề
            for line in file:
                columns = line.strip().split(',')
                file_username = columns[0]
                file_password = columns[1]
                file_algorithm = columns[2]
                
                # Mã hóa mật khẩu người dùng nhập với thuật toán tương ứng
                hashed_password = hash_password(password, file_algorithm)
                
                # Kiểm tra tên đăng nhập và mật khẩu đã mã hóa
                if file_username == username and file_password == hashed_password:
                    return True  # Đăng nhập thành công
    return False  # Đăng nhập thất bại

# Chương trình chính để kiểm tra đăng nhập
def login():
    un = username.get()
    pw = password.get()
    
    # Kiểm tra tài khoản
    if check_account(un, pw):
        print(f"Đăng nhập thành công với tài khoản '{un}'.")
    else:
        print("Đăng nhập thất bại. Tên đăng nhập hoặc mật khẩu không đúng.")

# Tạo nút
btnttk = Button(window, text="Đăng nhập", command=login)
btnttk.grid(column=1, row=3)

# Hiển thị
window.geometry('800x600')
window.mainloop()
