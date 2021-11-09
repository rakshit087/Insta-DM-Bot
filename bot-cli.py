from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
import pyperclip

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument('log-level=3')

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(random.choice([5, 6, 7, 8, 9]))
        username_input = bot.find_element(By.NAME,'username')
        password_input = bot.find_element(By.NAME,'password')
        username_input.clear()
        password_input.clear()
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)
        print("ALMOST THERE\n")
        time.sleep(random.choice([5, 6, 7, 8, 9]))
        try:
            bot.find_element(By.CLASS_NAME,'HoLwm').click()
        except:
            pass
        try:
            bot.find_element(By.ID,'slfErrorAlert')
            return 0
        except:
            pass
        print('Logged In')
        return 1

    def userSearch(self, user):
        print("SEARCHING USER\n")
        bot = self.bot
        bot.get('https://www.instagram.com/direct/new/')
        time.sleep(random.choice([5, 6, 7, 8, 9]))
        try:
            bot.find_element(By.CLASS_NAME,'HoLwm').click()
        except:
            pass
        input_box = bot.find_element(By.NAME,'queryBox')
        input_box.send_keys(user)
        time.sleep(random.choice([5, 6, 7, 8, 9]))
        try:
            input_box.send_keys(Keys.TAB)
            time.sleep(2)
            bot.switch_to.active_element.click()
            time.sleep(random.choice([5, 6, 7, 8, 9]))
            bot.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div[2]/div/button').click()
        except:
            print('If you are seeing this, it means bot needs an update')
            return 0
        time.sleep(random.choice([5, 6, 7, 8, 9]))

    def sendMessage(self, message):
        bot = self.bot
        try:
            messageArea = bot.find_element(By.TAG_NAME,'textarea')
            messageArea.send_keys(Keys.CONTROL+'v')
            messageArea.send_keys(Keys.RETURN)
            time.sleep(random.choice([5, 6, 7, 8, 9]))
        except:
            return 0
        return 1

if __name__ == '__main__':
    username = 'your_username'
    password = 'your_password'
    message = 'your_message'
    usernames = 'space seprated usernames'
    pyperclip.copy(message)
    Insta = InstagramBot(username, password)
    status = Insta.login()
    if(status == 0):
         print("Login Not Successfull")
    userlist = list(usernames.split(" "))
    ec = 0
    sc = 0
    for i in userlist:
        Insta.userSearch(i)
        x = Insta.sendMessage(message)
        if(x == 0):
            ec = ec+1
        else:
            sc = sc+1
        print("Messages Sent = ")
        print(sc)
        print("Messages ERROR = ")
        print(ec)
    print("done")

