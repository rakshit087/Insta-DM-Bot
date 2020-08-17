from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import eel

eel.init('Frontend')

class InstagramBot:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome(executable_path='chromedriver.exe')

    def login(self):
        bot=self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        eel.sleep(random.choice([5, 6, 7, 8, 9]))
        username_input=bot.find_element_by_name('username')
        password_input=bot.find_element_by_name('password')
        username_input.clear()
        password_input.clear()
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)
        print("ALMOST THERE\n")
        eel.sleep(5)
        try:
            loginstatus =  bot.find_element_by_id('slfErrorAlert')
            return 0
        except:
            pass
        try:
            NotNowButton = bot.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
            NotNowButton.click()
        except:
            pass
        return 1
        

    def userSearch(self,user):
        print("SEARCHING USER\n")
        bot = self.bot
        bot.get('https://www.instagram.com/' + user + '/')
        eel.sleep(5)
        
    def sendMessage(self,message):
        bot = self.bot
        try:
            messageButton = bot.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > div._862NM > div > button')
            messageButton.click()
            eel.sleep(5)
        except:
            return 0
        try:
            NotNowButton = bot.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.bIiDR')
            NotNowButton.click()
        except:
            pass
        eel.sleep(1)
        try:
            messageArea = bot.find_element_by_css_selector('#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi > textarea')
            messageArea.send_keys(message)
            messageArea.send_keys(Keys.RETURN)
            eel.sleep(2)
        except:
            return 0
        return 1
    
#Main Function
@eel.expose
def runBot(username, password,usernames,message):
    eel.sleep(3)
    Insta = InstagramBot(username,password)
    status = Insta.login()
    if(status==0):
        eel.status("Login Not Successfull")
        return "Login Not Successfull"
    userlist = list(usernames.split(" "))
    eel.status("Sending Messages")
    ec=0
    sc=0
    for i in userlist:
        Insta.userSearch(i)
        x=Insta.sendMessage(message)
        if(x==0):
            ec=ec+1
        else:
            sc=sc+1
        print("Messages Sent = ")
        print(sc)
        print("Messages ERROR = ")
        print(ec)
        eel.messageStatus(sc,ec)
    eel.status("done")

eel.start('index.html',size=(1100,720),port=8085)