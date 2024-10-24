from tkinter import *
import os
import hashlib
import random

# Xây dựng giao diện
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

# Cài đặt các Control
lb = Label(window, text="Tạo tài khoản", font=("Arial Bold", 20))
lb.grid(column=1, row=0)

lb1 = Label(window, text="Tên đăng nhập", font=("Arial Bold", 15))
lb1.grid(column=0, row=1)
username = Entry(window, width=100)
username.grid(column=1, row=1)

lb2 = Label(window, text="Mật khẩu", font=("Arial Bold", 15))
lb2.grid(column=0, row=2)
password = Entry(window, show="*", width=100)  # Ẩn mật khẩu
password.grid(column=1, row=2)

# Định nghĩa hàm chọn thuật toán và mã hóa mật khẩu
def hash_password(password):
    hash_algorithms = ['md5', 'sha1', 'sha256', 'sha512']
    chosen_algorithm = random.choice(hash_algorithms)  # Chọn ngẫu nhiên 1 thuật toán băm
    hash_object = getattr(hashlib, chosen_algorithm)(password.encode('utf-8'))
    return hash_object.hexdigest(), chosen_algorithm

# Định nghĩa hàm kiểm tra xem tài khoản đã tồn tại hay chưa
def account_exists(username):
    filename = 'CSDL.csv'
    if os.path.exists(filename):
        with open(filename, mode='r', newline='') as file:
            for line in file:
                columns = line.strip().split(',')
                if columns[0] == username:
                    return True
    return False

# Định nghĩa hàm lưu tài khoản vào file 
def save_account(username, password):
    filename = 'CSDL.csv'
    # Kiểm tra xem tài khoản đã tồn tại hay chưa
    if account_exists(username):
        print(f"Tài khoản '{username}' đã tồn tại trong hệ thống. Vui lòng chọn tên đăng nhập khác.")
        return
    # Kiểm tra file đã tồn tại chưa
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as file:
            file.write('Tên đăng nhập,Mật khẩu,Thuật toán\n')

    # Mã hóa mật khẩu
    hashed_password, algorithm = hash_password(password)

    # Ghi tài khoản vào file
    with open(filename, mode='a', newline='') as file:
        file.write(f'{username},{hashed_password},{algorithm}\n')
    print(f"Tài khoản '{username}' đã được lưu vào {filename} với thuật toán hash {algorithm}.")

# Chương trình chính để nhập thông tin tài khoản
def signup():
    un = username.get()
    pw = password.get()
    # Lưu tài khoản vào file
    save_account(un, pw)

# Tạo nút
btnttk = Button(window, text="Tạo tài khoản", command=signup)
btnttk.grid(column=1, row=3)

# Hiển thị
window.geometry('800x600')
window.mainloop()
