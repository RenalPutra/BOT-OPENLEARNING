from unittest import expectedFailure
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
from config.spawn import *

#melakukan login pada halaman pertama
def login():
    global driver
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.clear()
    username.send_keys(user)
    password.clear()
    password.send_keys(passwd)
    tombol = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    print(tombol)

#masuk pada modulsistem operasi
def masuk_modul():
    global driver
    button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ol-top-bar"]/ol-top-bar/div/nav/div[2]/ul/li[2]/top-bar-button/button'))).click()
    print(button2)
    button3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='Sistem Operasi']"))).click()
    print(button3)
    button4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="portal-container"]/portal-page/ol-top-bar/div/nav/div[2]/ul/li[2]/a'))).click()
    print(button4)

#melakukan login untuk masuk ke dalam sistem operasi
def login2():
    global driver
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.clear()
    username.send_keys(user)
    password.clear()
    password.send_keys(passwd)
    button5 = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[2]/div/div/div/div[3]/div[2]/form/button"))).click()
    print(button5)

#masuk ke dalam materi sistem oeprasi dan membuka keseluruhan pintu modul
def masuk_materi():
    global driver
    button6 = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Learning Modules"))).click()
    print(button6)
    time.sleep(5)
    # x_path = '//*[@id="module-display-layer"]/div/module-display/module-set/div/div/div[{0}]/module-container/module-title-bar/div'.format(angka)
    # button7 = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, x_path))).click()
    for i in range (1, 14):
        x_path = '//*[@id="module-display-layer"]/div/module-display/module-set/div/div/div[{0}]/module-container/module-title-bar/div'.format(i)
        button7 = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, x_path))).click()
        print(button7)
   
    # a = soup.find('div', {'class' : 'mv-module-title in-use'})
    # if a == button7:
    #     pass
    # else:
    #     print(button7)

#mulai mengerjakan modul
def proses_modul():
    global driver
    x_path2= '//*[@id="module-display-layer"]/div/module-display/module-set/div/div/div[{0}]/module-container/module-content/div/div[2]/ul/li[1]/module-display-page-link'.format(jenis_modul)
    button8 = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, x_path2))).click()
    print(button8)
    time.sleep(2)
    # slideku = jumlah_slide
    for i in range (jumlah_slide):
        for i in range(100):
            driver.execute_script("window.scrollBy(0, 200)","")
            time.sleep(0.01)
        try:
            button9 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-traversal-mount"]/div/div[2]/a'))).click()
            print(button9)
            time.sleep(5)
        except:
            button10 = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='css-1c9knll-Button-NextButtonComponent efmladu3']"))).click()
            print(button10)
            time.sleep(5)
