#!/usr/bin/env python3

import random

# ヘッダを出力
print("Content-Type: text/html")
print("")

# ランダムな数を取得
no = random.randint(1, 6)
# 画面に出力
print("""
<html>
<head><title>Dice</title></head>
<body>
    <h1>{num}</h1>
</body>
</html>
""".format(num=no))
