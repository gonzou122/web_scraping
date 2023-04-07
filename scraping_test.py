import time
from selenium import webdriver

driver = webdriver.Chrome("C:/Users/1000228034/Desktop/scraping/chromedriver.exe") # WebDriverのインスタンスを作成 pathを指定
driver.get('https://www.yahoo.co.jp/') # URLを指定してブラウザを開く
time.sleep(2) # 2秒待機
search_box = driver.find_element_by_name('p') # name属性で検索ボックスを特定
search_box.send_keys('スクレイピング') # 検索ボックスにテキストを入力
search_box.submit() # 検索文言の送信（検索ボタンを押すのと同じ）
time.sleep(2) # 2秒待機
driver.quit() # ブラウザを閉じる