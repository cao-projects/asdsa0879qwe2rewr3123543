
from time import sleep
from os import getcwd as getCwd
from os.path import join as pathJoin
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Web driver initialization

browserPath = pathJoin(getCwd(), "chromedriver")
driverService = Service(browserPath)
driver = webdriver.Chrome(service=driverService)

# Login Data

url = "https://docs.google.com/forms/d/e/1FAIpQLSe5ekHO_69K00YDQkEW-6w1dFEFePMpQuvR9ZfflJhIGz-mSA/viewform"
user_email = "bs10230405"
user_password = "azw@548394"

# Test Data
file_name = "rangoli.jpeg"
user_phone = "1234567890"
test_email = "bill@mail.com"
test_date = "2022-11-23"
test_name = "Bill Smith"
size_color = "medium red"

# locators

btn_next_page_xpath = "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div"
txt_email_id = "identifierId"
txt_password_xpath = "//input[@name='password']"
btn_next_password_xpath = "//*[@id='identifierNext']/div/button"
btn_first_page_xpath = "//*[@id='passwordNext']/div/button"
btn_clear_form_xpath = "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[2]/div/span/span"
btn_clear_form_warn_xpath = "/html/body/div[2]/div/div[2]/div[3]/div[2]"
radio_new_customer_id = "i5"
radio_shoe_xpath = "//*[@data-value='Clothing and Shoes']"
radio_units_4_xpath = "//*[@data-value='4']"
txt_size_color_xpath = "//textarea[@aria-label='Your answer']"
radio_find_yes_id = "i39"
txt_name_xpath = "//input[@aria-labelledby='i45']"
txt_date_xpath = "//input[@type='date']"
txt_email_xpath = "//input[@type='email']"
radio_notification_email_xpath =  "//*[@data-value='Email']"
btn_add_file_xpath = "//*[@aria-label='Add file']"
iframe_xpath = "//*[@id=':0.contentEl']/iframe"
txt_file_xpath = "//input[@type='file']"
btn_upload_xpath = "//*[@id='picker:ap:0']"
txt_phone_xpath = "//input[@type='text']"
radio_sms_no_xpath = "//*[@id='i12']"
btn_submit_xpath = "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div[2]"
txt_message_xpath = "/html/body/div[1]/div[2]/div[1]/div/div[3]"

# test execution

driver.get(url)

# User login
txt_email = driver.find_element(By.ID,txt_email_id )
txt_email.send_keys(user_email)
driver.find_element(By.XPATH, btn_next_password_xpath).click()

password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, txt_password_xpath )))
password_input.send_keys(user_password)

driver.find_element(By.XPATH, btn_first_page_xpath).click()

#  Clear the user data
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, btn_clear_form_xpath))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, btn_clear_form_warn_xpath))).click()
sleep(3)

# User Input

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, radio_new_customer_id))).click()

driver.find_element(By.XPATH, radio_shoe_xpath ).click()
driver.find_element(By.XPATH, radio_units_4_xpath).click()
driver.find_element(By.XPATH, txt_size_color_xpath).send_keys("size_color")
driver.find_element(By.ID, radio_find_yes_id).click()
driver.find_element(By.XPATH, txt_name_xpath).send_keys(test_name)
driver.find_element(By.XPATH, txt_date_xpath).send_keys(test_date)
driver.find_element(By.XPATH, radio_notification_email_xpath).click()
driver.find_element(By.XPATH, txt_email_xpath).send_keys(test_email)

# Upload file

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, btn_add_file_xpath))).click()
iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, iframe_xpath)))
driver.switch_to.frame(iframe)
choose_file = driver.find_element(By.XPATH, txt_file_xpath)
driver.execute_script('arguments[0].style =""; arguments[0].style.display="block"; arguments[0].style.visibility="visible";', choose_file)
file_path = pathJoin(getCwd(), file_name)
sleep(1)
choose_file.send_keys(file_path)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, btn_upload_xpath))).click()

# wait for the file to be uploaded
sleep(3)
driver.switch_to.parent_frame()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, btn_next_page_xpath))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, txt_phone_xpath))).send_keys(user_phone)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, radio_sms_no_xpath))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, btn_submit_xpath))).click()

act_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, txt_message_xpath))).text

if "Thanks!" in act_message:
    print("Test Passed")
    assert True
else:
    print("Test Failed")
    assert False

driver.quit()
