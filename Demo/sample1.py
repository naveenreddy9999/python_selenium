from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.amazon.in/")
# driver.find_element(By.NAME,"q").send_keys("facebook")
# driver.find_element(By.NAME,"q").send_keys(Keys.ENTER)
# driver.find_element(By.XPATH,"(//input[@type='submit'])[3]").click()

print(driver.current_url)
print(driver.title)
# driver.close()


