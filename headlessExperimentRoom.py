from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument('-headless')

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1, 
    "profile.default_content_setting_values.notifications": 1 
})

url = "https://fujino-fpu.github.io/Experimental/ExperimentRoom2Ver3test.html"

driver = webdriver.Chrome(chrome_options=option,executable_path="/usr/bin/chromedriver")

driver.get(url)

driver.implicitly_wait(5)

cam = driver.find_element_by_id("VideoList")
seleect_cam = Select(cam)
seleect_cam.select_by_index(1)

mic = driver.find_element_by_id("AudioList")
select_mic = Select(mic)
select_mic.select_by_index(0)

button_start = driver.find_element_by_id("local-Start")
button_start.click()

wait = WebDriverWait(driver, 30)
button_join = wait.until(expected_conditions.element_to_be_clickable((By.ID, "make-call")))

button_join.click()
