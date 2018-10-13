from Crypto.Cipher import AES
import base64

# 暗号化したいデータとパスワードを設定
message = "自分がして欲しいと思うことを人にもするように。"
password="xxxxxxxx"
iv = "L3f4mlTJtCIPV9af"
mode = AES.MODE_CBC

# 特定の長さの倍数にするため空白でデータを埋める関数
def mkpad(s, size):
    s = s.encode("utf-8")
    pad = b' ' * (size -len(s) % size)
    return s + pad

# 暗号化する
def encrypt(password, data):
    # 特定の長さに調節する
    password = mkpad(password, 16)
    data = mkpad(data, 16)
    password = password[:16]
    # 暗号化
    aes = AES.new(password, mode, iv)
    data_cipher = aes.encrypt(data)
    return base64.b64encode(data_cipher).decode("utf-8")

# 復号化する
def decrypt(password, encdata):
    # パスワードの文字数を調節
    password = mkpad(password, 16)
    password = password[:16]
    # 復号化
    aes = AES.new(password, mode, iv)
    encdata = base64.b64decode(encdata)
    data = aes.decrypt(encdata)
    return data.decode("utf-8")

# 暗号化する
enc = encrypt(password, message)
# 復号化する
dec = decrypt(password, enc)

# 結果を表示する
print("暗号化:", enc)
print("復号化:", dec)
