kuge: ラズパイでもスクレイピングをしたいあなたに
==================================================================
seleniumを用いるときいちいち文章を書くのが面倒だと思う人のためのちょっとしたなにかです。

コード量の削減に加えraspberry pi環境下とその他環境下でのseleniumを使ったスクレイピングコードの移動をシームレスに行うことが出来るようにします。


由来
------
名前の由来は「ク」ロームドライバーバイナリー「ゲ」ッターで公家（kuge）です。

普段はchromedriver_binaryモジュールを使っているのですがraspberry piのようなARM環境下ではchromedriver_binaryモジュールを使えないということに気づいて作りました。

Installation
-------------

**ARM以外**

    $pip install chrome_binary
    $pip install selenium

を行った後プロジェクトフォルダに直接kuge.pyをおき、利用するソースコード内で

    >>> import kuge

を行ってください

**Raspberry piのようなARM系**
    
    $pip install selenium
    $apt install chromium-chromedriver
    
を行った後プロジェクトフォルダに直接kuge.pyをおき、利用するソースコード内で

    >>> import kuge

を行ってください


API
-----

    kuge.get(is_headless=True, is_photo=True, path_to_chrome_driver=""): -> WebDriver
    >>> import kuge
    >>> browser = kuge.get(Falese, True)

is_headless: bool = True
  - ブラウザをヘッドレスモードで開くか
  
is_photo: bool = True
  - ブラウザで画像を読み込むか
    
path_to_chrome_driver: str = ""
  - 普段は使いません。どうしても自分でchromedriverのパスを指定したいときはここで指定します。


欠点
------

raspberry piの時try exceptを使って某モジュールのインポートの処理を飛ばしているので例外が握りつぶされる懸念があります。（多分大丈夫）
お気をつけください。

.. _`the repository`: https://github.com/Futafi/kuge.git
