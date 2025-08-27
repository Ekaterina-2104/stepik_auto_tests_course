import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)

    login = "email@gmail.com"
    password = "12345"
    browser.implicitly_wait(10)

    log_in_button = browser.find_element(By.XPATH, "//*[text()='Войти']")   # ember479
    log_in_button.click()

    input_login = browser.find_element(By.CSS_SELECTOR, "[name='login']")
    input_login.send_keys(login)
    input_password = browser.find_element(By.CSS_SELECTOR, "[name='password']")
    input_password.send_keys(password)

    enter_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    enter_button.click()

# ввод ответа
    time.sleep(5)
    input_answer = browser.find_element(By.CSS_SELECTOR, "textarea")
    input_answer.click()
    input_answer.send_keys(str(math.log(int(time.time()))))

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='submit-submission']"))
    )
    button.click()

# проверка фидбэка
    feedback = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='smart-hints__hint']"))).text
    assert feedback == "Correct!", "Неверно!"
