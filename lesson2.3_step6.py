from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/redirect_accept.html"


browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()
new_window = browser.window_handles[1]
time.sleep(2)
browser.switch_to.window(new_window)

x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = x_element.text
y = calc(x)

input_answer = browser.find_element(By.ID, "answer")
input_answer.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# успеваем скопировать код за 20 секунд
time.sleep(20)
# закрываем браузер после всех манипуляций
browser.quit()
