# 単語の出現回数をカウント
text = """
Keep on asking, and it willl be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking recieves, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

# 単語を区切る
text = text.replace(";", "")
text = text.replace(",", "")
text = text.replace(".", "")
words = text.split() # 空白で区切ってリスト型を作成

# 単語を数える
counter = {}

for w in words:
    ws = w.lower()
    if ws in counter:
        counter[ws] += 1
    else:
        counter[ws] = 1

# 結果を表示
for k, v in sorted(counter.items()):
    if v >= 3:
        print(k, v)
