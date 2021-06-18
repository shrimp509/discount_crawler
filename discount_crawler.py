from bs4 import BeautifulSoup
from selenium import webdriver
import requests

products = {
    "https://24h.pchome.com.tw/prod/DCAKC5-A9008B51P": 45000,
    "https://24h.pchome.com.tw/prod/DCAKC5-A900AXI1I": 45000,
    "https://24h.pchome.com.tw/prod/DCAKBA-A900B7JK4": 20000,
}

def run_scrawler():
    outputs = []
    driver = webdriver.Chrome('./chromedriver')

    for product_url, min_price in products.items():
        driver.get(product_url)
        soup = BeautifulSoup(driver.page_source)
        outputs.append(soup.title.string)
        price = soup.body.select("span#PriceTotal")[0].string

        if int(price) <= min_price:
            msg = "=> 特價中，現在 {} 比你訂的 {} 還便宜了，快來看看\n{}"
        else:
            msg = "=> 沒特價，現在是 {}，期待低於 {}，繼續等吧\n{}"

        outputs.append(msg.format(price, str(min_price), product_url))
        outputs.append('------')

    driver.quit()
    result = "\n".join(outputs)
    popup("爬蟲結果", result)

def popup(title, content):
    import platform
    if platform.system() == 'Windows':
        popup_windows(title, content)
    else:
        popup_mac(title, content)

def popup_windows(title, content):
    import ctypes
    return_value = ctypes.windll.user32.MessageBoxW(0, content, title, 0)

def popup_mac(title, content):
    import os
    mac_cmd = "osascript -e \'tell app \"System Events\" to display dialog \"{}\" with title \"{}\"\'".format(content, title)
    os.system(mac_cmd)

# MainFunctions
run_scrawler()
