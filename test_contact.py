import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pop_classes import ContactPage  # импортируем класс страницы
import os
import time


def test_contact_form_positive():
    # Настройка Chrome для CI (headless режим)
    chrome_options = Options()
    if os.getenv('CI'):  # Если запускается в CI
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    
    # Инициализация страницы
    page = ContactPage(driver)
    
    # Используем относительный путь для работы в CI
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(current_dir, 'index.html')
    page.open(f"file://{html_file}")
    
    page.fill_name("Alice")
    page.fill_email("dfdf@ава.rtgr")
    page.fill_message("Hello!")
    page.submit()

    time.sleep(3)
    assert page.is_success_displayed()

    driver.quit()