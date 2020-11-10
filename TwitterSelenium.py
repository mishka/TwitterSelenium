from time import sleep
from os import getcwd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Selectors:
    LoginUsername = 'session[username_or_email]'
    LoginPassword = 'session[password]'

    # The following is bull-shit!
    TweetBox = '.r-1dqxon3 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)'
    TweetButton = 'div.r-urgr8i:nth-child(4)'

class TwitterClient:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-infobars') # is this discontinued? not sure
        options.add_argument('--window-size=1280,900')
        options.add_argument('--dns-prefetch-disable')
        options.add_argument('--disable-setuid-sandbox')
        options.add_argument('user-data-dir=' + getcwd() + '/browser')
        self.driver = webdriver.Chrome(options = options)

    def quit(self):
        return self.driver.quit()

    def get(self, url):
        return self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

    def execute(self, script, element):
        return self.driver.execute_script(script, element)

    def find_name(self, selector):
        return self.driver.find_element_by_name(selector)

    def find_xpath(self, selector):
        return self.driver.find_element_by_xpath(selector)

    def find_css(self, selector):
        return self.driver.find_element_by_css_selector(selector)

    def login(self, username, password):
        # If the following is async, then this function should be changed
        self.get('https://twitter.com/login')
        sleep(3)

        if 'login' not in self.current_url():
            print('Already logged in, continuing…')
            return

        print('Logging in...')

        sleep(3)
        self.find_name(Selectors.LoginUsername).send_keys(username)
        pw = self.find_name(Selectors.LoginPassword)
        pw.send_keys(password)

        sleep(3)
        pw.send_keys(Keys.ENTER)

    def tweet(self, text = None, media = None):
        self.get('https://twitter.com/compose/tweet')
        sleep(3)

        if text:
            self.find_css(Selectors.TweetBox).send_keys(text)
            sleep(1.5)

        if media:
            for path in media:
                file_input = self.find_xpath("//input[@type='file']")
                self.execute("arguments[0].style.display = 'block';", file_input)

                file_input.send_keys(path)
                sleep(0.5)
        
        if text or media:
            self.find_css(Selectors.TweetButton).click()
