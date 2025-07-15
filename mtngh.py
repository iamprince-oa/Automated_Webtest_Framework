import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Setting up the browser environment
web = webdriver.Firefox()

#Opening the link in browser
web.get("https://mtn.com.gh/")
web.implicitly_wait(10)

#accept_button = web.find_element(By.CLASS_NAME, "cky-btn-accept")
#accept_button.click()

#Finding the pop-up and closing it
try:
    first_element = web.find_element(By.CLASS_NAME, "cky-banner-btn-close")
    first_element.click()
    print("Pop-Up Closed")
except:
    print("Pop-Up Not Found")

#Finding the Business link and clicking on it
second_element = web.find_element(By.LINK_TEXT, "BUSINESS")
second_element.click()

third_element = web.find_element(By.CLASS_NAME, "yello-heading")
print(third_element.text)

forth_element = web.find_element(By.LINK_TEXT, "Contact")
forth_element.click()

first_name_input = web.find_element(By.NAME, "vwp-first-name")
first_name_input.send_keys("Prince")

last_name_input = web.find_element(By.NAME, "vwp-surname")
last_name_input.send_keys("Owusu")

contact_number_input = web.find_element(By.NAME, "vwp-contact-number")
contact_number_input.send_keys("0593130530")

email_input = web.find_element(By.NAME, "vwp-email-address")
email_input.send_keys("owusup484@gmail.com")

business_name_input = web.find_element(By.NAME, "vwp-business-name")
business_name_input.send_keys("MTN-Ghana-Attachment")

input("Complete The re Captcha and Press Enter to continue")

web.find_element(By.ID, "recaptcha-verify-button").click()

request_callback = web.find_element(By.CLASS_NAME, "mtn-callback-form-btn")
request_callback.click()

print("Test Completed and successful")