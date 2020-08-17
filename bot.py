from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(executable_path='chromedriver.exe')

    def login(self):
        bot=self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(random.choice([5, 6, 7, 8, 9]))
        username_input=bot.find_element_by_name('username')
        password_input=bot.find_element_by_name('password')
        username_input.clear()
        password_input.clear()
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)
        print("ALMOST THERE\n")
        time.sleep(5)
        try:
            NotNowButton = bot.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
            NotNowButton.click()
            print("SUCCESSFULLY LOGGED IN\n")
        except:
            pass
        time.sleep(5)

    def userSearch(self,user):
        print("SEARCHING USER\n")
        bot = self.bot
        bot.get('https://www.instagram.com/' + user + '/')
        time.sleep(5)
        
    def sendMessage(self,message):
        bot = self.bot
        messageButton = bot.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > div._862NM > div > button')
        messageButton.click()
        time.sleep(5)
        try:
            NotNowButton = bot.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.bIiDR')
            NotNowButton.click()
        except:
            pass
        time.sleep(5)
        messageArea = bot.find_element_by_css_selector('#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi > textarea')
        messageArea.send_keys(message)
        time.sleep(5)
        messageArea.send_keys(Keys.RETURN)
        time.sleep(5)
    
#Main Function

Insta = InstagramBot('','')
Insta.login()
Insta.userSearch('')
Insta.sendMessage('')