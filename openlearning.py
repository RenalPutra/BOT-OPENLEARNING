from mechanicalsoup import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time
import os
import wget
from config.config import *
from pathlib import Path
from playsound import playsound

#Running chrome fake
os.system('cls')
try: 
    print(readme.read())
except:
    print(readme.read())
isi_data()
driver.get("https://www.openlearning.com/")
driver.maximize_window()



#Memulai memilih materi
try:
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="base-page-container"]/div[1]/div[2]/div[2]/a[1]'))).click()
    print(button)
    time.sleep(5)
except:
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="base-page-container"]/div[1]/div[2]/div[2]/a[1]'))).click()
    print(button)
    time.sleep(5)

#Pemanggilan Modul

login()
time.sleep(5)

masuk_modul()
time.sleep(5)

login2()
time.sleep(5)

masuk_materi()
time.sleep(8)
        
proses_modul()
audio = Path().cwd() / "music/undertale.mp3"
for i in range(5):
    playsound(audio)





















