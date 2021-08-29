"""
    SAMPLE CODE TAKEN FROM
    
    https://thinkdiff.net/how-to-scrap-data-from-javascript-based-website-using-python-selenium-and-headless-web-driver-531c7fe0c01f
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located as itmloc
from time import sleep

chrome_driver_path = "E:/PYTHONS/DRIVER/chromedriver.exe"
chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options
)

driver.get('https://www.nseindia.com/get-quotes/equity?symbol=PSUBNKBEES')

wait = WebDriverWait(driver, 20)

wait.until(itmloc((By.ID, "#quoteLtp")))
# sleep(10)
PRI = driver.find_element_by_id('#quoteLtp')
driver.close()
print(PRI)
