from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Кликаем на кнопку
    button = browser.find_element_by_tag_name("button")
    button.click()
    
    # Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # Ждем загрузки новой вкладки
    time.sleep(1)
    
    # Считаем значение по формуле и вводим в поле
    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = calc(x)
    
    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)
    
    # Визуально осматриваем форму
    time.sleep(1)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
     
finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла