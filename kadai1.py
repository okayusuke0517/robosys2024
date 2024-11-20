#!/user/bin/python3
# SPDX-FileCopyrightText: 2024 Yusuke Oka <s23C1031KK@s.chibakoudai.jp>
# SPDX-License-Identifier: BSD-3-Clause


import random

def play_attimuite_hoi():
    directions = ['上', '下', '左', '右']
    user_wins, comp_wins = 0, 0

    for i in range(1, 4):  # 3回繰り返す
        input(f"{i}回目: Enterを押すと開始します...")
        print(f"あっち向いてホイ！ -> {random.choice(directions)}")
        
        user_input = input("勝っていたら'y'、負けていたら'n'を入力してください: ").strip().lower()
        if user_input == 'y':
            user_wins += 1
            print("あなたの勝ち！")
        elif user_input == 'n':
            comp_wins += 1
            print("コンピュータの勝ち！")
        else:
            print("無効な入力です。このラウンドは無効です。")

    # 最終結果を表示
    result = "あなたの勝利！" if user_wins > comp_wins else "あなたの負け！" if comp_wins > user_wins else "引き分け！"
    print(f"\n最終結果: {result}")

if __name__ == "__main__":
    play_attimuite_hoi()

