#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Yusuke Oka
# SPDX-License-Identifier: BSD-3-Clause

import random
import time
def k1_test2():
    directions = ['上','下','左','右']

    print("自動的に開始")
    for i in range(3):
        print("あっち向いてホイ")
        time.sleep(3)
        print(f"  -> {random.choice(directions)}")

if __name__ =="__main__":
    k1_test2()
    