from selenium import webdriver
import time

print("Execution Started")
driver = webdriver.Chrome()  # Replace with your preferred browser
driver.get("https://google.com")  # Replace with the target URL
time.sleep(10)
# Perform actions on the webpage here

driver.quit()
print("Execution Done")