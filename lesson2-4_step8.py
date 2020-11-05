from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ждем, пока цена будет 100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    
    # Кликаем на кнопку
    button = browser.find_element_by_id("book")
    button.click()
    
    # Скроллим к кнопке
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    # Считаем значение по формуле и вводим в поле
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    
    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)
    
    # Визуально осматриваем форму
    time.sleep(1)
    
    # Отправляем заполненную форму
    button.click()
     
finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла