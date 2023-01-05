from selenium import webdriver

from Demo.pages.signup_page import SignInPage

driver = webdriver.Firefox()
driver.maximize_window()

print('pass1')
driver.get("https://www.google.com/")
signup_page = SignInPage(driver)
signup_page.sign()
signup_page.enter()

# driver.quit()
