import requests
import time
from konlpy.tag import Mecab
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json

mecab = Mecab()
options = Options()
options.add_argument('user-agent=Mozilla/5.0')
driver = webdriver.Chrome('./chromedriver', options=options)

def connect_to(url):
    driver.get(url)

def get_nouns():
    iframes = driver.find_elements_by_tag_name('iframe')
    driver.switch_to.frame(iframes[6])
    titles = driver.find_elements_by_tag_name('a')
    t = ""
    for title in titles:
        t+=title.get_attribute('innerHTML')
    nouns = mecab.nouns(t)
    filtered = []
    for noun in nouns:
        if len(noun)>1:
            filtered.append(noun)
    return filtered 

def go_next():
    driver.switch_to.default_content()
    next_button = driver.find_element_by_class_name('_btn_nxt')
    next_button.click()
    time.sleep(1)


nouns = []
connect_to('https://newsstand.naver.com/')
nouns.extend(get_nouns())

for i in range(51):
    go_next()
    nouns.extend(get_nouns())

with open('nouns.json', 'w', encoding='utf-8') as f:
    json.dump(nouns, f, ensure_ascii=False, indent=4)





