import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import winsound

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

def alarm():
    try:
        while True:
            winsound.Beep(2000, 500)
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass 
        

def exception():
    driver.quit()
    print("An error occured. Press Ctrl + C to stop alarm.")
    alarm()
    time.sleep(10)
    exit()

PATH = "C:/Users/Philip/Desktop/Programme/Digital Attendance Substitute/chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver = webdriver.Chrome(PATH, options=chrome_options)

driver.get("https://moodle.migy.de/moodle/blocks/exa2fa/login/")

# login
n = 0
while True:
    try:
        username = driver.find_element_by_id("username")
    except:
        time.sleep(10)
        driver.refresh()
        n += 1
        # about 10 sec per ideration 15 min = ~120 iterations
        if n >= 100:
            print("Can't reach service. Press Ctrl + C to stop alarm.")
            alarm()
    else:
        username = driver.find_element_by_id("username")
        break

username.send_keys("MogilskiPhi")

password = driver.find_element_by_id("password")
password.send_keys("(mcjWb[7>U{R*en6")

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