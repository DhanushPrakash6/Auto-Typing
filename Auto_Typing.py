from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
string = input("ENTER PLAYER NAME: ")
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://10ff.net/login")
wait = WebDriverWait(driver, 600)
inp_xpath = '//input[@id="username"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

input_box.send_keys(string + Keys.ENTER)
for i in range(1,80):
    read_xpath = '//div[@class="place"]/span[' + str(i) + ']'
    read_box_try = wait.until(EC.presence_of_element_located((By.XPATH, read_xpath)))
    read_box = driver.find_elements_by_xpath('//div[@class="place"]/span[' + str(i) + ']')[0].text
    if(i==1):
        time.sleep(12)
    inp_newbox = '// input[ @ type = "text"]'
    input_now = wait.until(EC.presence_of_element_located((By.XPATH, inp_newbox)))
    input_now.send_keys(read_box + Keys.SPACE)