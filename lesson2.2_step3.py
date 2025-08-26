from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "https://suninjuly.github.io/selects1.html"


browser = webdriver.Chrome()
browser.get(link)

num1_element = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
num1 = int(num1_element.text)
num2_element = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
num2 = int(num2_element.text)
summ = str(num1 + num2)


select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(summ)


button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()


# успеваем скопировать код за 20 секунд
time.sleep(20)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла
