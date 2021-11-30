from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

url = "https://fujino-fpu.github.io/Experimental/ExperimentRoom2Ver3test.html"

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")

driver.get(url)

# 画面表示を最大5秒まで待つ
driver.implicitly_wait(5)

cam = driver.find_element_by_id("VideoList")
seleect_cam = Select(cam)
seleect_cam.select_by_index(1)

mic = driver.find_element_by_id("AudioList")
select_mic = Select(mic)
select_mic.select_by_index(0)

button_start = driver.find_element_by_id("local-Start")
button_start.click()

wait = WebDriverWait(driver, 10)
button_join = wait.until(expected_conditions.element_to_be_clickable((By.ID, "make-call")))

button_join.click()


