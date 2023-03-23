from tkinter import *
import math

# Hàm tính n, phi(n), e và d
def calculate_params(p, q):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537  # Số nguyên tố thứ hai lớn nhất sau 2
    while True:
        gcd, x, y = math.gcd(e, phi_n), 0, 0
        if gcd == 1:
            break
        e += 2
    d = pow(e, -1, phi_n)
    return n, e, d

# Hàm mã hóa văn bản
def encrypt_text(text, n, e):
    encrypted = [pow(ord(c), e, n) for c in text]
    return encrypted

# Hàm giải mã văn bản
def decrypt_text(encrypted, n, d):
    decrypted = [chr(pow(c, d, n)) for c in encrypted]
    decrypted_text = "".join(decrypted)
    return decrypted_text

# Hàm xử lý sự kiện khi nhấn nút Mã hóa
def encrypt_button_click():
    p = int(p_entry.get())
    q = int(q_entry.get())
    n, e, d = calculate_params(p, q)
    message = message_entry.get()
    encrypted = encrypt_text(message, n, e)
    encrypted_text.set(" ".join([str(c) for c in encrypted]))

# Hàm xử lý sự kiện khi nhấn nút Giải mã
def decrypt_button_click():
    p = int(p_entry.get())
    q = int(q_entry.get())
    n, e, d = calculate_params(p, q)
    encrypted = [int(c) for c in encrypted_text.get().split()]
    decrypted = decrypt_text(encrypted, n, d)
    decrypted_text.set(str(decrypted))

# Tạo giao diện đồ họa
root = Tk()
root.title("Mã hóa RSA")

# Tạo các điều khiển nhập liệu và nút Mã hóa/Giải mã
p_label = Label(root, text="p:")
p_label.grid(row=0, column=0)
p_entry = Entry(root)
p_entry.grid(row=0, column=1)

q_label = Label(root, text="q:")
q_label.grid(row=1, column=0)
q_entry= Entry(root)
q_entry.grid(row=1, column=1)

message_label = Label(root, text="Văn bản:")
message_label.grid(row=2, column=0)
message_entry = Entry(root)
message_entry.grid(row=2, column=1)

encrypt_button = Button(root, text="Mã hóa", command=encrypt_button_click)
encrypt_button.grid(row=3, column=0)

decrypt_button = Button(root, text="Giải mã", command=decrypt_button_click)
decrypt_button.grid(row=3, column=1)

encrypted_label = Label(root, text="Văn bản đã mã hóa:")
encrypted_label.grid(row=4, column=0)
encrypted_text = StringVar()
encrypted_entry = Entry(root, textvariable=encrypted_text)
encrypted_entry.grid(row=4, column=1)

decrypted_label = Label(root, text="Văn bản đã giải mã:")
decrypted_label.grid(row=5, column=0)
decrypted_text = StringVar()
decrypted_entry = Entry(root, textvariable=decrypted_text)
decrypted_entry.grid(row=5, column=1)

root.mainloop()
