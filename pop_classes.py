from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver): #как конструктор в ооп
        self.driver = driver #как this.

    def open(self, url):
        self.driver.get(url)

    def find(self, by, value): #Находит элемент на странице по селектору.
        return self.driver.find_element(by, value)

    def click(self, by, value):
        self.find(by, value).click()

    def type(self, by, value, text):
        elem = self.find(by, value)
        elem.clear()
        elem.send_keys(text)


class ContactPage(BasePage): #наследовать
    NAME_INPUT = (By.ID, "name") #кортеж
    EMAIL_INPUT = (By.ID, "email")
    MESSAGE_INPUT = (By.ID, "message")
    SUBMIT_BTN = (By.ID, "submit-btn")
    ERROR_MSG = (By.ID, "error")
    SUCCESS_MSG = (By.ID, "success")

    def fill_name(self, name):
        self.type(*self.NAME_INPUT, name)

    def fill_email(self, email):
        self.type(*self.EMAIL_INPUT, email)

    def fill_message(self, message):
        self.type(*self.MESSAGE_INPUT, message)

    def submit(self):
        self.click(*self.SUBMIT_BTN)

    def is_error_displayed(self):
        return self.find(*self.ERROR_MSG).is_displayed()

    def is_success_displayed(self):
        return self.find(*self.SUCCESS_MSG).is_displayed()

def test_contact_form_positive(driver):
    page = ContactPage(driver)
    page.open("file:///Users/anastasiaanikina/Desktop/Уник/4_course/testing/test4/index.html")

    page.fill_name("Alice")
    page.fill_email("alice@mail.com")
    page.fill_message("Hello!")
    page.submit()

    assert page.is_success_displayed()