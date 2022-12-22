from ast import Try
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
    time.sleep(5)
    try:
        button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ol-top-bar"]/ol-top-bar/div/nav/div[2]/ul/li[3]/top-bar-button/button'))).click()
        print(button2)
    except:
        button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ol-top-bar"]/ol-top-bar/div/nav/div[3]/ul/li[3]/top-bar-button/button/span[1]'))).click()
        print(button2)
    button3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ol-top-bar"]/ol-top-bar/div/nav/div[2]/ul/li[3]/top-bar-dropdown/div[1]/section/div[2]/div/div[2]/ul/li[6]/a'))).click()
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
    tombol = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    print(tombol)

#masuk ke dalam materi sistem oeprasi dan membuka keseluruhan pintu modul
def masuk_materi():
    global driver
    button5 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="course-links"]/div/div/div/div/ul/li[5]/a'))).click()
    print(button5)
    time.sleep(5)
    # x_path = '//*[@id="module-display-layer"]/div/module-display/module-set/div/div/div[{0}]/module-container/module-title-bar/div'.format(angka)
    # button7 = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, x_path))).click()
    def bukamodul():
        driver.execute_script("window.scrollTo(0, 0)","")
        for i in range(1,18):
            x_path = '//*[@id="module-display-layer"]/div/module-display/module-set/div/div/div[{0}]/module-container/module-title-bar/div'.format(i)
            button6 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path))).click()
            print(button6)
            time.sleep(0.01)
    cek = True        
    while cek:
        print("\n")
        tanya = input("apakah modul yang mau kamu buka udah muncul? [y/n] : ")
        print("\n")
        if tanya == "y":
            break
        elif tanya == "n":
            bukamodul()
        else:
            print("Bukan itu yang saya tanyakan bang! Lu paham ga sih? 😡")
   
    # a = soup.find('div', {'class' : 'mv-module-title in-use'})
    # if a == button7:
    #     pass
    # else:
    #     print(button7)

#mulai mengerjakan modul
def proses_modul():
    global driver

    
    try:
        x_path2 = '//*[@id="module-display-layer"]/div/module-display/module-set/div/div/div[{0}]/module-container/module-content/div/div[2]/ul/li[1]'.format(jenis_modul)
        button8 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path2))).click()
        print(button8)
    except:
        x_path2 = '//*[@id="module-display-layer"]/div/module-display/module-set/div/div/div[{0}]/module-container/module-content/div/div[2]/ul/li[1]'.format(jenis_modul)
        button8 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x_path2))).click()
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
            button10 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#page-traversal-mount > div > div:nth-child(2) > a']']"))).click()
            print(button10)
            time.sleep(5)
            