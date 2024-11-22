#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Yusuke Oka
# SPDX-License-Identifier: BSD-3-Clause

import random

def play_game():
    directions = ['上','下','左','右']

    for i in range(1, 4):
        input(f"\n{i}回目: Enterを押すと開始")
        print(f"あっち向いてホイ　> {random.choice(directions)}")

        
        while True:
            user_input = input("勝っていたらｙ、負けていたらｎをおせ")
            if user_input == 'y':
                print("あなたの勝ち")
                break
            elif user_input == 'n':
                print("コンピュータの勝ち")
                break

    input("\n3回終わったのでEnterを押して終了")

if __name__ =="__main__":
    play_game()




