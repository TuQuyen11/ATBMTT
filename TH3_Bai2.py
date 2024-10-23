#Bước 1: viết hàm sinh khóa
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    original_phi = phi
    x0, x1 = 0, 1
    while e > 1:
        q = e // phi
        phi, e = e % phi, phi
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += original_phi
    return x1

def is_prime(n):
    if n <= 1:
        return False
    #2 và 3 là số nguyên tố
    if n <= 3:
        return True
    #loại bỏ số chẵn và bội của 3
    if n % 2 == 0 or n % 3 == 0: 
        return False 
    i = 5
    #kiểm tra căn bậc 2 của n
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_candidate(length):
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1  # Đảm bảo p là số lẻ và có đủ số bit
    return p

def generate_prime_number(length):
    p = 5
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p

def generate_rsa_keys(keysize):
    p = generate_prime_number(keysize // 2)
    q = generate_prime_number(keysize // 2)

    n = p * q  # Khóa công khai
    phi = (p - 1) * (q - 1)

    # Chọn e
    e = 65537  # Thường chọn 65537 vì nó là số nguyên tố và tối ưu

    # Tính d
    d = mod_inverse(e, phi)

    return (e, n), (d, n)  # Trả về khóa công khai và khóa riêng

# Sử dụng hàm
public_key = generate_rsa_keys(1024)
private_key = generate_rsa_keys(1024)
print("Khóa công khai (e, n):", public_key)
print("Khóa riêng (d, n):", private_key)

#Bước 2: viết hàm mã hóa và hàm giải mã
def encrypt(plain_text, public_key):
    e, n = public_key
    plain_text_bytes = plain_text.encode()
    # Chuyển đổi từng byte thành số và mã hóa
    cipher_text = [pow(byte, e, n) for byte in plain_text_bytes]
    return cipher_text

def decrypt(cipher_text, private_key):
    d, n = private_key
    # Giải mã từng số thành byte
    decrypted_bytes = [pow(byte, d, n) for byte in cipher_text]
    return bytes(decrypted_bytes).decode()

# Sử dụng hàm
public_key, private_key = generate_rsa_keys(1024)

# Mã hóa
message = "Đây là văn bản bí mật."
cipher_text = encrypt(message, public_key)
print("Dữ liệu đã mã hóa:", cipher_text)

# Giải mã
decrypted_message = decrypt(cipher_text, private_key)
print("Dữ liệu đã giải mã:", decrypted_message)
