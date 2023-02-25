from selenium import webdriver
import time
from getPassword import getPassword
# from getPassword import getDate
from buf import getNickname

def Twitch_sugnup(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(executable_path="C:\\Users\\amil2\\OneDrive\\Рабочий стол\\TT\\chrome\\chromedriver.exe", options=options)
    
    try:
        date = getDate()
        driver.get(url=url)
        time.sleep(3)
        driver.find_element_by_xpath("//div[contains(text(), 'Регистрация')]").click()
        # //input[@aria-label="Выберите имя пользователя"]
        name = driver.find_element_by_xpath("//input[@aria-label='Выберите имя пользователя']")
        name.send_keys(getNickname())
        password = driver.find_element_by_xpath("//input[@aria-label='Придумайте надежный пароль']")
        password.send_keys(getPassword())
        while 1:
            pass
        # driver.execute_script("window.open('https://temp-mail.org/en/');")
        # driver.switch_to.window(driver.window_handles[1])
        
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def main():
    Twitch_sugnup("https://www.twitch.tv/")


if __name__ == "__main__":
    main()
