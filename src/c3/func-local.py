# 関数の外側でvalueに100を代入
value = 100

def cahngeValue():
    # 関数の内側でvalueを変更
    value = 20

cahngeValue()
print("value=", value)
