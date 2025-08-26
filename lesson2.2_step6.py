from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"


browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = x_element.text
y = calc(x)

input_answer = browser.find_element(By.ID, "answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)
input_answer.send_keys(y)

robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
robotCheckbox.click()
robotsRule = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
robotsRule.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()


# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла
