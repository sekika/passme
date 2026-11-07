# Passme: PC とモバイルで使えるパスワード生成ツール

**Passme**は、パスワードそのものを保存することなく、多くのサイトで利用できる強力でユニークなパスワードを生成するツールです。Python 製のコマンドライン版、Flutter 製の iOS アプリ、ブラウザーで利用できる JavaScript 版があります。

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
*   **ポータブル:** [iOS アプリ](https://apps.apple.com/us/app/password-passme/id6830239169)や、生成した [HTML/JavaScript ファイル](https://sekika.github.io/passme/javascript/)を使い、スマートフォンに Python をインストールせずにパスワードを生成できます。
*   **ベンダーロックインなし:** 標準的でオープンなアルゴリズムを使用しています。このソフトウェアの開発が終了しても、既知の計算ロジックを使ってパスワードを復元できます。

## 利用できるバージョン

* **Python / CLI 版:** PC でサイトキーを管理し、パスワードを生成します。導入と操作方法は以下を参照してください。
* **iOS アプリ:** [App Store](https://apps.apple.com/us/app/password-passme/id6830239169) からインストールし、サイトキーファイルを取り込みます。[モバイル利用案内](https://sekika.github.io/passme/mobile/)を参照してください。
* **JavaScript 版:** `passme html` で HTML ファイルを生成し、モバイル端末を含むブラウザーで利用します。[JavaScript 版の利用案内](https://sekika.github.io/passme/javascript/)を参照してください。

## インストール（Python / CLI 版）

コマンドライン版の実行には Python 3 が必要です。

```bash
pip install passme
```

## クイックスタート（Python / CLI 版）

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

詳しい使い方、設定オプション、モバイルでの利用（iOS アプリと JavaScript 版）、セキュリティの詳細については、以下のドキュメントを参照してください。

[**https://sekika.github.io/passme/**](https://sekika.github.io/passme/) ([日本語翻訳](https://sekika-github-io.translate.goog/passme/?_x_tr_sl=en&_x_tr_tl=ja&_x_tr_hl=ja))

## 開発経緯

2017年の[公開](https://sekika.github.io/2017/05/09/Password/)以来、作者は既存のパスワード管理システムからPassmeに移行し、2026年現在まで安全に利用を続けています。現在、100以上のサイトのパスワードをこのツールで管理しています。

## ライセンス

このソフトウェアは[MITライセンス](LICENSE.txt)のもとで公開されています。

作者: [Katsutoshi Seki](https://github.com/sekika)

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/sekika/passme)
