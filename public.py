import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def exception():
    driver.quit()
    print("An error occured. Check your inputs. If this problem persists contact the developer.")
    time.sleep(10)
    exit()

# get data
with open('./config.json') as f:
    data = json.load(f)

username = data["username"]
password = data["password"]

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://moodle.migy.de/moodle/blocks/exa2fa/login/")

# login
usernameField = driver.find_element_by_id("username")
usernameField.send_keys(username)

passwordField = driver.find_element_by_id("password")
passwordField.send_keys(password)

loginbtn = driver.find_element_by_id("loginbtn")
loginbtn.click()

# courseroom
try:
    courselist = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "frontpage-course-list"))
    )
except:
    exception()


classroom = courselist.find_element_by_link_text("Klassenzimmer 9c Fernunterricht")
classroom.click()

# attendance
try:
    module = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "module-19941"))
    )
except:
    exception()

attendance = module.find_element_by_link_text("Anwesenheit").click()

# record attendance
try:
    record = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Anwesenheit erfassen"))
    )
except:
    exception()

record.click()

try:
    present = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_status_213"))
    )
except:
    exception()

present.click()

try:
    submitbtn = driver.find_element_by_id("id_submitbutton")
    submitbtn.click()
except:
    exception()

driver.quit()
print("Login successful")
time.sleep(3)