from termcolor import colored
from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import string

ab = open('ip.txt', 'r').read().splitlines()
ba = len(ab)
ra = random.randint(1200, 13000)
ra2 = random.randint(120, 1300)
char_set = string.ascii_lowercase
char_set2 = string.ascii_uppercase

for i in range(0, ba):
  try:
    a = PROXY = f"{ab[0+i]}"
    s = Service('/Users/machintoshd/.wdm/drivers/chromedriver/go/95.0.4638.17/chromedriver')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % a)
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.maximize_window()
    driver.get(f'https://share.socialearn.co/u/raview69')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="masthead"]/div/div/div/div[2]/div/div[1]/a').click()
    sleep(2)
    a = driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    driver.quit()
    print(colored(" Signup Success", "green"))
  except:
    print(colored(" Signup Gagal", "red"))
def testUserLocationDenver(self):
	self.chrome.get(self.url)
	search = self.chrome.find_element_by_id('user-city')
	self.assertIn('Denver', search.text)
