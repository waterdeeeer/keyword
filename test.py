import requests
from collections import Counter
from konlpy.tag import Mecab
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


mecab = Mecab()

options = Options()
options.add_argument('user-agent=Mozilla/5.0')
driver = webdriver.Chrome('./chromedriver', options=options)

driver.get('https://newsstand.naver.com/?list=ct1&pcode=215')
driver.implicitly_wait(3)

iframes = driver.find_elements_by_tag_name('iframe')


driver.switch_to.frame(iframes[6])

titles = driver.find_elements_by_tag_name('a')

t = ""

for title in titles:
    t+=title.get_attribute('innerHTML')

nouns = mecab.nouns(t)


print(nouns)





