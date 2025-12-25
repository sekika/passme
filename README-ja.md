# Passme: コマンドラインのパスワード管理ツール

**Passme**はコマンドラインで利用するパスワード管理ツールです。パスワードそのものを保存することなく、多くのサイトで利用できる強力でユニークなパスワードを生成します。

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/sekika/passme/blob/master/README.md)
[![ja](https://img.shields.io/badge/lang-ja-blue.svg)](https://github.com/sekika/passme/blob/master/README-ja.md)

<img alt="Passme illustration" src="https://sekika.github.io/passme/passme.svg" style="width: min(100%, 600px);  height: auto; margin:auto; display: block" />

暗号化された保管庫（ボールト）にパスワードを保存する代わりに、Passmeは設定ファイルに保存されたサイト固有のシード（**サイトキー**）と、あなただけが知っている**マスターパスワード**を使い、毎回決定論的にパスワードを生成します。

> **サイトキー + マスターパスワード = パスワード**

**[ドキュメント全文を読む](https://sekika.github.io/passme/)**

## 主な特徴

*   **ステートレス:** パスワードはその場で計算されます。サイトキーファイルとマスターパスワードさえあれば、どこでもパスワードを生成できます。
*   **セキュア:** オフラインでの総当たり攻撃（ブルートフォースアタック）が困難です。攻撃者は、推測したパスワードが正しいかどうかを実際のログインページで試さない限り検証できません（あなたのパスワードを一つでも知らない限り）。
*   **柔軟:** サイトごとに長さ、文字セット（英数字、記号など）、ハッシュ化アルゴリズムをカスタマイズできます。
*   **ポータブル:** スタンドアロンで動作する[HTML/Javascriptファイル](https://sekika.github.io/passme/passme.html)を生成する機能があり、Pythonがないモバイル端末でもパスワードを生成できます。
*   **ベンダーロックインなし:** 標準的でオープンなアルゴリズムを使用しています。このソフトウェアの開発が終了しても、既知の計算ロジックを使ってパスワードを復元できます。

## インストール

Passmeの実行にはPython 3が必要です。

```bash
pip install passme
```

## クイックスタート

### 1. 初期設定
`passme`を実行し、サイトキーファイルの保存場所を設定します。

```bash
> passme
Filename to save site keys: /path/to/your/sitekeys.txt
```

### 2. サイトの追加
サービス（例: Google）の新しいエントリを作成します。文字セットや長さを定義できます。

```bash
> passme add
Site name: google
Character (an): 
Password length (14): 
...
```

### 3. パスワードの生成
パスワードを取得するには、`passme`に続けてサイト名を入力します。

```bash
> passme google
Master password: [マスターパスワードを入力]
(生成されたパスワードはクリップボードにコピーされます)
```

## セキュリティに関する警告

*   **マスターパスワードを忘れないでください。**
*   **サイトキーファイルを失くさないでください。**

Passmeはパスワードを保存しないため、「パスワードを忘れた場合」の回復機能はありません。マスターパスワードかサイトキーファイルのどちらかを失うと、生成されたすべてのアカウントにアクセスできなくなります。サイトキーファイルは**プライベート**なGitリポジトリで管理することを強く推奨します。

## ドキュメント

詳しい使い方、設定オプション、モバイルでの利用（Javascript版）、セキュリティの詳細については、以下のドキュメントを参照してください。

[**https://sekika.github.io/passme/**](https://sekika.github.io/passme/)

## 開発経緯

2017年の[公開](https://sekika.github.io/2017/05/09/Password/)以来、作者は既存のパスワード管理システムからPassmeに移行し、2025年現在まで安全に利用を続けています。現在、100以上のサイトのパスワードをこのツールで管理しています。

## ライセンス

このソフトウェアは[MITライセンス](LICENSE.txt)のもとで公開されています。

作者: [Katsutoshi Seki](https://github.com/sekika)