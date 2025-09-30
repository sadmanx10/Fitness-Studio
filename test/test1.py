from multiprocessing.managers import Value
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("http://127.0.0.1:8000/")

time.sleep(2)

#driver.find_element(By.LINK_TEXT,"login").click()

driver.find_element(By.NAME, "username").send_keys("sadman")
driver.find_element(By.NAME, "password").send_keys("sadman")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(4)
driver.find_element(By.LINK_TEXT, "Challenge").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Coaching").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Membership").click()
time.sleep(3)
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Shop").click()
time.sleep(3)
time.sleep(2)
driver.find_element(By.LINK_TEXT, "About Us").click()
time.sleep(3)


driver.quit()
