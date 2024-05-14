from selenium import webdriver
from selenium.webdriver.common.by import By


class RegisterUserError:

    url = 'http://dev.bootcamp.store.supersqa.com/my-account/'
    invalid_email = 'abc@gmail'
    expected_msg = 'Error: Please provide a valid email address.'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def go_to_my_account(self):
        self.driver.get(self.url)

    def input_email(self):
        field = self.driver.find_element(By.ID, 'reg_email')
        field.send_keys(self.invalid_email)

    def input_password(self):
        field = self.driver.find_element(By.ID, 'reg_password')
        field.send_keys('dkjaflkdsjf')

    def click_login(self):
        self.driver.find_element(By.NAME, 'register').click()

    def verify_error_message(self):
        err_elm = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')
        displayed_err = err_elm.text
        assert displayed_err == self.expected_msg, "The displayed error is not expected."
        print("PASS")

    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_password()
        self.click_login()
        self.verify_error_message()
        self.driver.quit()

if __name__ == '__main__':

    obj = RegisterUserError()
    obj.main()
