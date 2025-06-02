import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select

#Locators
username_textbox = "username"
email_textbox= "email"
password_textbox = "//*[@type='password']"
bio_textbox = "bio"
country_drop_down = "country"
languages_drop_down = "languages"
interests_checkbox_group = "checkbox-group"
radio_button_options = "//*[@class='radio-item']/input"
show_confirm_alert = "//*[text()='Show Confirm']"


edge_driver_path = "C:\\Users\\parde\\PycharmProjects\\selenium-practice\\msedgedriver.exe"
edge_options =Options()
edge_options.use_chromium = True # Need to learn about Chromium and other option webview

service = Service(executable_path=edge_driver_path)

driver = webdriver.Edge(service=service)
driver.maximize_window()
driver.get("https://techbeamers.com/selenium-practice-test-page/")

def scroll_to_element(ele):
    driver.execute_script("arguments[0].scrollIntoView(true);",ele)

#Task 1
scroll_to_element(driver.find_element(By.ID,username_textbox))
driver.find_element(By.ID,username_textbox).send_keys("test_username")
scroll_to_element(driver.find_element(By.NAME,email_textbox))
driver.find_element(By.NAME,email_textbox).send_keys("test_email")
scroll_to_element(driver.find_element(By.XPATH,password_textbox))
driver.find_element(By.XPATH,password_textbox).send_keys("test_password")
scroll_to_element(driver.find_element(By.ID,bio_textbox))
driver.find_element(By.ID,bio_textbox).send_keys("test_bio")


#Task 2
scroll_to_element(driver.find_element(By.ID, country_drop_down))
Select(driver.find_element(By.ID,country_drop_down)).select_by_visible_text("Japan")
Select(driver.find_element(By.ID,languages_drop_down)).select_by_visible_text("English")
Select(driver.find_element(By.ID,languages_drop_down)).select_by_visible_text("French")

#Task 3
scroll_to_element(driver.find_element(By.CLASS_NAME, interests_checkbox_group))
# def check_check_boxes(options):
#     for i in options.split(","):
#         scroll_to_element(driver.find_element(By.ID,i))
#         driver.find_element(By.ID,i).click()
# check_check_boxes("sports,music,reading")


#Task 4
def select_radio_button(text_option):
    radio_options = driver.find_elements(By.XPATH,radio_button_options)
    for i in radio_options:
        if i.get_attribute("value")== text_option:
            i.click()

select_radio_button("male")

#Task 5
show_alert = driver.find_element(By.XPATH, show_confirm_alert)
scroll_to_element(show_alert)
show_alert.click()
alert = Alert(driver)
# print(alert.text)
alert.accept()





time.sleep(5)