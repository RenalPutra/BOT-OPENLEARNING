from unittest import expectedFailure
from mechanicalsoup import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os
import wget


#Memanggil chrome fake
driver = webdriver.Chrome(ChromeDriverManager().install())
#Melakukan penginoutan data dan materi tujuan
readme = open("require.txt", "r")
user = input("Masukkan username OPL anda : ")
passwd = input("Masukkan password OPL anda : ")
jenis_modul = input("Modul berapa yang ingin di baca? (1 - 18) : ")
jumlah_slide = int(input("Masukkan Jumlah slide modul keseluruhan: "))
def isi_data():
    global user, passwd, jenis_modul, jumlah_slide

    
    