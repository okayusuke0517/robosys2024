# k1コマンド
![test](https://github.com/okayusuke0517/robosys2024/actions/workflows/test.yml/badge.svg)

これはロボットシステム学の課題１で作成したもので、「あっち向いてホイ」のゲームができる。

## 説明・概要

k1では日本の遊びである「あっち向いてホイ」を再現したゲームを遊ぶことができる。まず自分が遊びたい回数をコマンドを実行するときに一緒に数字で入力する。コンピュータが「あっち向いてホイ」という文字を出すのでプレイヤーはその文字が出たら上下左右どちらかを向く。そのあとプレイヤーが前を見るとコンピュータが指した方向が表示されており、これを指定した回数繰り返すと「終了」という文字とともに終わる。また自分が指示を出す側と受ける側どちらにもなれるのが利点だ。

## 目的

「あっち向いてホイ」を一人で遊べる。

## ダウンロードして移動

リポジトリをクローン
```bash
git clone https://github.com/okayusuke0517/robosys2024.git
```

ディレクトリに移動
```bash
cd robosys2024
```

## 使い方

実行方法の例1
```bash
echo 数字 | python3 k1
```

実行方法の例２
```bash
echo 数字 | ./k1
```

## 必要なソフトウェア

- Python3
  - テスト済みバージョン: 3.7～3.10

## テストしたこと

k1に書いたコードをk1\_test1 , k1\_test2 , k1\_test3\_all のように途中、途中で区切りそこまでのコードが動くかを3.7～3.10のバージョンでそれぞれtest.ymlを用いてテストをした。また最後にk1で全てのコードをテストした。

## テスト環境

 - Ubuntu 22.04.5 LTS

## ライセンス

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
© 2024 Yusuke Oka

## 参照サイト

- https://osksn2.hep.sci.osaka-u.ac.jp/~taku/osx/python/readfile.html      
- https://machine-learning-skill-up.com/knowledge/python%E6%A8%99%E6%BA%96%E5%85%A5%E5%8A%9B%E3%81%AE%E5%9F%BA%E6%9C%AC%E3%81%A8%E6%B4%BB%E7%94%A8%E6%96%B9%E6%B3%95%E3%82%92%E5%BE%B9%E5%BA%95%E8%A7%A3%E8%AA%AC%EF%BC%81
- https://magazine.techacademy.jp/magazine/15821
