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
富士ゼロックス、ロボで書類電子化　米新興と新会社 https://www.nikkei.com/article/DGXMZO63367690S0A900C2916M00/
スタートバーンと芸大、芸術情報デジタル化、EC連携 https://www.nikkei.com/article/DGXMZO63365130S0A900C2EE9000/
消毒ロボット、ただいま走行中　茨城・つくば市 https://www.nikkei.com/article/DGXMZO63357930S0A900C2L60000/
先天性無歯症の治療薬を開発へ　京大発スタートアップ https://www.nikkei.com/article/DGXMZO63347950S0A900C2916M00/
起業希望者の「壁打ち」役に、長野・松本に県が拠点 https://www.nikkei.com/article/DGXMZO63335540S0A900C2L21000/
Voicy、有料会員限定の音声番組 https://www.nikkei.com/article/DGXMZO63343140S0A900C2X30000/
タイの衣料通販ポメロ、インドネシアなどで実店舗 https://www.nikkei.com/article/DGXMZO63342610S0A900C2FFJ000/
スクー、単位取得できるオンライン講座　福岡大と連携 https://www.nikkei.com/article/DGXMZO63341290S0A900C2000000/
サッカー元代表鈴木氏のAuB、腸内新菌を製品化へ https://www.nikkei.com/article/DGXMZO63338110S0A900C2XY0000/
オリィ研究所、川田テクノロジーズと遠隔バリスタロボ https://www.nikkei.com/article/DGXMZO63337940S0A900C2XY0000/
ICCサミット、廃棄物アートのMAGOが優勝 https://www.nikkei.com/article/DGXMZO63337860S0A900C2XY0000/
ココナラ、代表を2人体制に　創業者南氏は会長に https://www.nikkei.com/article/DGXMZO63337700S0A900C2XY0000/
お茶の入れ方、IoTで最適に　スタートアップがポット発売 https://www.nikkei.com/article/DGXMZO63337500S0A900C2XY0000/
伊藤忠、中古スマホのレンタル　SIMフリー端末活用 https://www.nikkei.com/article/DGXMZO63296570R00C20A9TJ1000/
スタートアップ大型イベント、リーナーとメディが優勝 https://www.nikkei.com/article/DGXMZO63293370R00C20A9XY0000/
トラック運転手を人気職業に　買い物代行で社会貢献 https://www.nikkei.com/article/DGXMZO63096380X20C20A8TL3000/
ブロックチェーン企業に再びマネー　実用化に期待 https://www.nikkei.com/article/DGXMZO63245970R30C20A8SHA100/
作業現場でも在宅勤務でも　「複合現実」ゴーグル浸透 https://www.nikkei.com/article/DGXMZO63251960R30C20A8SHA100/
グッドパッチがオンライン白板、リモートワークでも共同作業しやすく https://www.nikkei.com/article/DGXMZO63252710R30C20A8XY0000/
「通話を文字化して要約」サービス　コロナで導入急増 https://www.nikkei.com/article/DGXMZO63010110V20C20A8000000/
世界から来たれサッポロへ、「金のタマゴ」3割増計画 https://www.nikkei.com/article/DGXMZO63357760S0A900C2L41000/
新型コロナ、重症者ほど抗体少なく　1万6千人調査 https://www.nikkei.com/article/DGXMZO63345320S0A900C2000000/
HPE日本法人社長、レッドハット前社長の望月氏が就任 https://www.nikkei.com/article/DGXMZO63330710S0A900C2000000/
NHK、フレキシブルディスプレー省電力化　新材料開発 https://www.nikkei.com/article/DGXMZO63328980S0A900C2000000/
使用済み核燃料の中間貯蔵施設　安全審査「合格」 https://www.nikkei.com/article/DGXMZO63330100S0A900C2I00000/
台風9号、高い海水温で急激に発達　週内に次の台風も https://www.nikkei.com/article/DGXMZO63293230R00C20A9I00000/
新材料ゴム×プラスチック　夢かなうかブリヂストン https://www.nikkei.com/article/DGXMZO62791290Z10C20A8000000/
したたかな欧州、ガソリンスタンドより多いEV充電器 https://www.nikkei.com/article/DGXMZO62845960Q0A820C2000000/
温暖化ガス削減、積み上げ探る　審議会で議論開始 https://www.nikkei.com/article/DGXMZO63302740R00C20A9EE8000/
デンソーの欠陥、ホンダに波及　判断遅れメガリコール https://www.nikkei.com/article/DGXMZO62884950R20C20A8000000/
朽ちていく軍艦島　「廃虚の王」にふさわしい保存とは https://www.nikkei.com/article/DGXMZO62970530U0A820C2000000/
「通話を文字化して要約」サービス　コロナで導入急増 https://www.nikkei.com/article/DGXMZO63010110V20C20A8000000/
国際生物学五輪が初の遠隔開催、日本代表に金・銀 https://www.nikkei.com/article/DGXMZO63173420Y0A820C2000000/
第3のロケット発射準備　ハイブリッドで安全・エコ https://www.nikkei.com/article/DGXMZO63267200R30C20A8XY0000/
札幌に「リトルダッカ」爆誕？IT技術者は北を目指す https://www.nikkei.com/article/DGXMZO63260770R30C20A8L41000/
がん免疫薬の効果を予測、精度は9割　国立がん研究センターなど https://www.nikkei.com/article/DGXMZO63243520R30C20A8I00000/
世界遺産・軍艦島、崩壊へのカウントダウンが始まった https://www.nikkei.com/article/DGXMZO62970300U0A820C2000000/
LIXIL、玄関ドアを後付けで「自動ドア」にする新商品 https://www.nikkei.com/article/DGXMZO63008480V20C20A8000000/
「検査のわな」が引き起こすPCR神学論争 https://www.nikkei.com/article/DGXMZO63057600W0A820C2I00000/
冷房が不快なワケ　湿度と日射熱に気をつけよう https://www.nikkei.com/article/DGXMZO63018570V20C20A8000000/
世界から来たれサッポロへ、「金のタマゴ」3割増計画 https://www.nikkei.com/article/DGXMZO63357760S0A900C2L41000/
「通話を文字化して要約」サービス　コロナで導入急増 https://www.nikkei.com/article/DGXMZO63010110V20C20A8000000/
札幌に「リトルダッカ」爆誕？IT技術者は北を目指す https://www.nikkei.com/article/DGXMZO63260770R30C20A8L41000/
アウルとカタギリ・コーポレーションが資本業務提携 https://www.nikkei.com/article/DGXMZO63250590R30C20A8L41000/
スペスデン、高校生向け教育動画配信サービス https://www.nikkei.com/article/DGXMZO63172730Y0A820C2FFT000/
東芝、生活習慣病リスクを6年先まで予測 https://www.nikkei.com/article/DGXMZO63184360Y0A820C2X20000/
AIの学び、高精度　データ100分の1でも画像認識 https://www.nikkei.com/article/DGXMZO63133810X20C20A8TJM000/
アマスポーツにプロ並み映像、AIが変える中継技術 https://www.nikkei.com/article/DGXMZO63099780X20C20A8X13000/
AIカメラで負担軽減、au店舗でアウルが実証 https://www.nikkei.com/article/DGXMZO63118470X20C20A8L41000/
Zoff、AI新興と提携　スマートグラス共同開発 https://www.nikkei.com/article/DGXMZO63023340V20C20A8TJ1000/
エクサウィザーズ、AIカメラ提供開始　子どもの笑顔を自動で撮影 https://www.nikkei.com/article/DGXMZO63032670V20C20A8XY0000/
AI開発のアルベルト　大企業と長期で協業 https://www.nikkei.com/article/DGXMZO62940040R20C20A8TJP000/
ゼンリン系、バス内の混雑度を計測　「カメラ×AI」で https://www.nikkei.com/article/DGXMZO62902940R20C20A8TJ1000/
フラクタ、AIで水処理のコスト削減　栗田工業と https://www.nikkei.com/article/DGXMZO62884450R20C20A8X20000/
驚異のAIスーパー　唐揚げにハイボールをリコメンド https://www.nikkei.com/article/DGXMZO62714760X10C20A8000000/
高専×AI、学生の起業進む　香川高専で2例目 https://www.nikkei.com/article/DGXMZO62863320Q0A820C2LA0000/
メッセナゴヤ、オンラインで代替 https://www.nikkei.com/article/DGXMZO62857310Q0A820C2L91000/
前橋市、スーパーシティ申請へ　デジタル都市目指す https://www.nikkei.com/article/DGXMZO62848320Q0A820C2L60000/
札幌のインディテール、牛乳の質を高める実証実験 https://www.nikkei.com/article/DGXMZO62848270Q0A820C2L41000/
品川区が独自給付金を円滑給付　AIやLINE活用で https://www.nikkei.com/article/DGXMZO62276080U0A800C2000000/
アルプスアルパイン、損保ジャパンと保険商品開発 https://www.nikkei.com/article/DGXMZO63349810S0A900C2X20000/
ソフトバンク、戸建て宅配ボックス事業化へ実証実験 https://www.nikkei.com/article/DGXMZO63148490Y0A820C2000000/
CO2濃度で「3密」検知のIoTシステム、産学共同で実験 https://www.nikkei.com/article/DGXMZO63094980X20C20A8000000/
KDDI、仙台高専と協定　5G環境を整備 https://www.nikkei.com/article/DGXMZO63074170W0A820C2L01000/
混雑データが変える人流　街の「密」を丸ごと可視化 https://www.nikkei.com/article/DGXMZO62742700Y0A810C2000000/
テレワーク、VPN暗証番号流出　国内38社に不正接続 https://www.nikkei.com/article/DGXMZO62994110U0A820C2MM8000/
スタンプラリー「3密」回避　観光×デジタルの新価値 https://www.nikkei.com/article/DGXMZO62743930Y0A810C2000000/
札幌のインディテール、牛乳の質を高める実証実験 https://www.nikkei.com/article/DGXMZO62848270Q0A820C2L41000/
サンクレエ、自動運転の歩行器を開発 https://www.nikkei.com/article/DGXMZO62649780U0A810C2L41000/
トヨタ北海道、製造設備にIoT 370台遠隔監視 https://www.nikkei.com/article/DGXMZO62260100U0A800C2000000/
ワイン用ブドウをAI栽培、調和技研が北海道で実証 https://www.nikkei.com/article/DGXMZO62230600T00C20A8L41000/
投資家に聞く　コロナ後注目のセンシング技術 https://www.nikkei.com/article/DGXMZO61480170U0A710C2000000/
東芝テック、帯広の百貨店などにスマートレシート https://www.nikkei.com/article/DGXMZO61849390S0A720C2L41000/
エヌビディアがインテルの時価総額を抜いたのはなぜ？ https://www.nikkei.com/article/DGXMZO61668680X10C20A7000000/
東芝デジタル社長、実世界のデータ起点にDX https://www.nikkei.com/article/DGXMZO61626350X10C20A7000000/
「暑いね」で扇風機オン、Amazonスマートプラグ https://www.nikkei.com/article/DGXMZO61573040W0A710C2000000/
IoT通信のソラコム、KDDIと格安5Gサービス https://www.nikkei.com/article/DGXMZO61502190U0A710C2X13000/
ホステルで長期滞在　アンドファクトリー、訪日客減で https://www.nikkei.com/article/DGXMZO61479640U0A710C2000000/
富士通が目指すDX伝道師　テレワーク起点に全社改革 https://www.nikkei.com/article/DGXMZO61282670Y0A700C2000000/
KDDI、産業向け格安5G　月額数百円から https://www.nikkei.com/article/DGXMZO61442040T10C20A7MM8000/