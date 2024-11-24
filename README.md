# k1.pyコマンド
![test](https://github.com/okayusuke0517/robosys2024/actions/workflows/test.yml/badge.svg)

これはロボットシステム学の課題１で作成したもので、「あっち向いてホイ」のゲームができる。

## 説明・概要

k1.pyでは日本の遊びである「あっち向いてホイ」を再現したゲームを遊部ことができる。コンピュータが「あっち向いてホイ」という文字を出すのでプレイヤーはその文字が出たら上下左右どちらかを向く。そのあとプレイヤーが前をみるとコンピュータが指した方向が表示されており、これを３回繰り返すと終了という文字とともに終わる。また自分が指示を出す側と受ける側どちらにもなれるのも利点だ。

## 目的

「あっち向いてホイ」を一人で遊べる。

## インストール方法

'''bash
リポジトリをクローン
git clone https://github.com/okayusuke0517/robosys2024.git

ディレクトリに移動
cd robosys2024'''

## 使い方

実行方法の例1

'''python3 k1.py'''

実行方法の例２

'''bash
権限を付与
chmod +x k1.py

実行
./k1.py'''

## 必要なソフトウェア

- Python3
  - テスト済みバージョン: 3.7～3.10
  - k1.pyを k1\_test1.py , k1\_test2.py , k1\_test3\_all.py
    の３回に分け、上記のバージョンでそれぞれテストした。  

## テスト環境

- Ubuntu 20.04.6 LTS

## ライセンス

*このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
*© 2024 Yusuke Oka
