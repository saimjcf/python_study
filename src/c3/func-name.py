# 関数の定義
def calcTime(dist, speed):
    t = dist / speed
    t = round(t, 1)
    print("dist:",dist)
    print("speed",speed)
    return t

# 通常の呼び出し
print( calcTime(500, 100))
# 名前付き引数の呼び出し
print( calcTime(dist=500, speed=100))
# 名前付き引数の呼び出し
print( calcTime(speed=100, dist=400))
