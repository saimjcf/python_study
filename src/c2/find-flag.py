# for構文をフラグで分岐する場合
# お弁当の食材データからリストを作成
foodstuff = ["Banana", "Mango", "Fish", "Carrot", "cabbage"]

# マンゴーがないか確認する
flag_found = False # マンゴがないかを確認する変数。初期値としてFalseを設定
for food in foodstuff: # food という変数に、foodstuffの値がひとつづつ入る。繰り返しのたびに新しい値が入る
    if food == "Mango":
        flag_found = True
        break

if flag_found:
    print("マンゴーが入ってます")
else:
    print("ありません")
