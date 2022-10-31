from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import credentials
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "katyperry"
USERNAME = credentials.insta_user
PASSWORD = credentials.insta_password
URL = "https://www.instagram.com/"


class InstaFollower:

    def __int__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get(URL)
        time.sleep(5)

        user_input = self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_input.send_keys(USERNAME)

        password_input = self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(PASSWORD)

        login_button = self.driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        time.sleep(3)

        not_now_button = self.driver.find_element("xpath",
                                                  '//*[@id="mount_0_0_Lb"]/div/div/div/div[1]/div/div/div/div['
                                                  '1]/section/main/div/div/div/div/button')
        not_now_button.click()
        time.sleep(3)

    def find_followers(self, similar_account):
        search_bar = self.driver.find_element("xpath",
                                              '//*[@id="mount_0_0_WK"]/div/div/div/div[1]/div/div/div/div['
                                              '1]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys(similar_account)
        search_bar.send_keys(Keys.RETURN)
        time.sleep(2)

        followers = self.driver.find_element("xpath",
                                             '//*[@id="mount_0_0_WK"]/div/div/div/div[1]/div/div/div/div['
                                             '1]/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()
        time.sleep(1)

        follower_list = self.driver.find_elements(By.CLASS_NAME,
                                                  "_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm")
        return follower_list

    def follow(self, follower):
        to_follow = follower.find_element(By.CLASS_NAME, "_aacl _aaco _aacw _aad6 _aade")
        to_follow.click()
        time.sleep(1)


bot = InstaFollower()
bot.login()
followers = bot.find_followers(SIMILAR_ACCOUNT)

for follower in followers:
    bot.follow(follower)

