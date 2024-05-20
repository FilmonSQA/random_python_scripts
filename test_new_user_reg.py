

from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random

driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = "http://dev.bootcamp.store.supersqa.com/my-account/"
email_filed_id = 'reg_email'
passwd_filed_id = 'reg_password'
logout_btn_css = 'li.woocommerce-MyAccount-navigation-link--customer-logout a'

driver.get(url)
email_filed_= driver.find_element(By.ID, email_filed_id)

letters = string.ascii_lowercase
rand_string = ''.join(random.choice(letters) for i in range(15))
random_email = rand_string + '@gmail.com'

email_filed_.send_keys(random_email)

password_field = driver.find_element(By.ID, passwd_filed_id)
password_field.send_keys('hellowsqa@123')

register_btn = driver.find_element(By.CSS_SELECTOR, 'button[value="Register"]')
register_btn.click()

try:
    logout_btn = driver.find_element(By.CSS_SELECTOR, logout_btn_css)
except:
    raise Exception("User not logged in after registering.")
if logout_btn.is_displayed():
    print("PASS.")
else:
    raise Exception("User not logged in after registering.")

