from selenium import webdriver
import os


def get(is_headless=True, is_photo=True, path_to_chrome_driver=""):
    options = webdriver.ChromeOptions()
    if is_headless:
        options.add_argument('--headless')
    if not is_photo:
        options.add_argument('--blink-settings=imagesEnabled=false')

    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--lang=ja')
    options.add_argument('--disable-desktop-notifications')

    # 現時点で拡張機能の使用は不可能だがGoogleがそのうち使えるようにしそうなのであらかじめdisableしておく
    options.add_argument("--disable-extensions")

    # windowsで実行したときのログ出力の抑制
    options.add_argument('--log-level=3')
    if os.environ.get("USER") == "root":
        options.add_argument('--no-sandbox')
    
    if path_to_chrome_driver:
        browser = webdriver.Chrome(executable_path=path_to_chrome_driver, options=options)
        browser.implicitly_wait(3)
        return browser

    try:
        import chromedriver_binary
    except ModuleNotFoundError:
        browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver', options=options)
    else:
        browser = webdriver.Chrome(options=options)

    browser.implicitly_wait(3)
    return browser
