from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Hello man you're in......!")
user_name = input("Enter Your Username or email :- ")
Password_of_user = input("Enter Your Password :- ")
Hashtag_to_search = input("Enter hastag to search and like :- ")

class twitter_bot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)

        email = bot.find_elements_by_name('session[username_or_email]')[1]
        password = bot.find_elements_by_name('session[password]')[1]
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password, Keys.ENTER)
        time.sleep(5)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=%23'+hashtag+'&src=typed_query')
        time.sleep(3)
        
        for w in range(1, 3):
            hearts = bot.find_elements_by_css_selector("svg.r-4qtqp9.r-yyyyoo.r-1xvli5t.r-dnmrzs.r-bnwqim.r-1plcrui.r-lrvibr.r-1hdv0qi")
            print(len(hearts))
            try:
                for i in range(2, len(hearts), 4):
                    hearts[i].click()
                    time.sleep(10)
            except Exception :
                time.sleep(10)
            
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)


ed = twitter_bot(user_name, Password_of_user)
ed.login()
ed.like_tweet(Hashtag_to_search)
