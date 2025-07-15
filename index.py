import os
from selenium import webdriver
#Setting Up The Environment Variable.
web = webdriver.Firefox() # type: ignore

#Opening The Browser And Navigating To The Website.
web.get("https://www.mtn.com.gh/")

get_page_source = web.page_source

#Getting The Page Source.
if "MTN" in get_page_source:
    print("MTN is in the page source.")
else:
    print("MTN is not in the page source.")
web.quit() # type: ignore
