from selenium import webdriver
import time
from getDate import getPassword
# from getPassword import getDate
from buf import getNickname

def Twitch_sugnup(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(executable_path="C:\\Users\\amil2\\OneDrive\\Рабочий стол\\TT\\chrome\\chromedriver.exe", options=options)
    
    try:
        driver.get(url=url)
        time.sleep(3)
        driver.find_element_by_xpath("//div[contains(text(), 'Регистрация')]").click()
        time.sleep(2)
        name = driver.find_element_by_xpath("//input[@aria-label='Выберите имя пользователя']")
        name.send_keys(getNickname())
        time.sleep(2)
        password = driver.find_element_by_xpath("//input[@aria-label='Придумайте надежный пароль']")
        password.send_keys(getPassword())
        time.sleep(2)
        driver.find_element_by_xpath("//div[contains(text(), 'Следующий шаг')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[contains(text(), 'Воспользуйтесь адресом эл. почты')]").click()
        time.sleep(2)
        driver.execute_script("window.open('https://temp-mail.org/en/');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        while 1:
            pass

        
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def main():
    Twitch_sugnup("https://www.twitch.tv/")


if __name__ == "__main__":
    main()
