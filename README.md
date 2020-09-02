# Pythonでwebスクレイピングをしてメールを送信する
日本経済新聞の個人的に興味がある分野のみでwebスクレイピングを行い、記事のタイトルとURLをメールで送信するプログラムを書きました。

## main.py
webスクレイピングで日本経済新聞内の特定分野に関して見出しとURLを取得後、メール本文用に見出しとURLの間に空白の追加と文末に改行を追加する。メール送信（TO_ADDRESSに送信）では件名に年月日を記録するようにしました。

## web_scraping.py
webスクレイピングを行うためのプログラムです。このプログラムでは以下の4つの分野でのみwebスクレイピングを行いましたが、日本経済新聞ではどの分野での同じ方法で見出しとURLを取得できます。

1. ビジネス / スタートアップ
2. テクノロジー / 最新技術
3. テクノロジー / AI
4. テクノロジー / IoT

## send_mail.py
メールを送信するためのプログラムです。プログラム内の'*'は各自のメールアドレスに書き換えてください。何か他の用途でもメール送信する機能を使用したい場合はsend_mail.pyからmail関数をインポートすることでメールを送信することも可能です。mail関数の引数について説明を記載します。

"""
mail("送信元メールアドレス", "送信先メールアドレス", "BCCのメールアドレス", "件名", "本文")
"""

### 実行結果（2020/09/03 実行時の結果）
2020年9月3日時点での実行結果について一部記載します。  
| 見出し | URL |
| ----  | --- |
|富士ゼロックス、ロボで書類電子化　米新興と新会社|https://www.nikkei.com/article/DGXMZO63367690S0A900C2916M00/|
|スタートバーンと芸大、芸術情報デジタル化、EC連携|https://www.nikkei.com/article/DGXMZO63365130S0A900C2EE9000/|
|消毒ロボット、ただいま走行中　茨城・つくば市|https://www.nikkei.com/article/DGXMZO63357930S0A900C2L60000/|
|先天性無歯症の治療薬を開発へ　京大発スタートアップ|https://www.nikkei.com/article/DGXMZO63347950S0A900C2916M00/|
|世界から来たれサッポロへ、「金のタマゴ」3割増計画|https://www.nikkei.com/article/DGXMZO63357760S0A900C2L41000/|
|使用済み核燃料の中間貯蔵施設　安全審査「合格」|https://www.nikkei.com/article/DGXMZO63330100S0A900C2I00000/|
|台風9号、高い海水温で急激に発達　週内に次の台風も|https://www.nikkei.com/article/DGXMZO63293230R00C20A9I00000/|
|「通話を文字化して要約」サービス　コロナで導入急増|https://www.nikkei.com/article/DGXMZO63010110V20C20A8000000/|
|札幌のインディテール、牛乳の質を高める実証実験|https://www.nikkei.com/article/DGXMZO62848270Q0A820C2L41000/|
|エヌビディアがインテルの時価総額を抜いたのはなぜ？|https://www.nikkei.com/article/DGXMZO61668680X10C20A7000000/|
|東芝デジタル社長、実世界のデータ起点にDX|https://www.nikkei.com/article/DGXMZO61626350X10C20A7000000/|
|「暑いね」で扇風機オン、Amazonスマートプラグ|https://www.nikkei.com/article/DGXMZO61573040W0A710C2000000/|
|IoT通信のソラコム、KDDIと格安5Gサービス|https://www.nikkei.com/article/DGXMZO61502190U0A710C2X13000/|
|ホステルで長期滞在　アンドファクトリー、訪日客減で|https://www.nikkei.com/article/DGXMZO61479640U0A710C2000000/|
|富士通が目指すDX伝道師　テレワーク起点に全社改革|https://www.nikkei.com/article/DGXMZO61282670Y0A700C2000000/|
|KDDI、産業向け格安5G　月額数百円から|https://www.nikkei.com/article/DGXMZO61442040T10C20A7MM8000/|