from selenium import webdriver
import time
from getDate import getPassword
from getDate import getDate
from fake_useragent import UserAgent


useragent = UserAgent()

def TikTok_sugnup(url):
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={useragent.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(executable_path="C:\\Users\\amil2\\OneDrive\\Рабочий стол\\TT\\chrome\\chromedriver.exe", options=options)
    
    try:
        date = getDate()
        print(f"{date=}")
        driver.get(url=url)
        time.sleep(3)
        driver.find_element_by_xpath("//div[contains(text(), 'Месяц')]").click()
        time.sleep(1)
        driver.find_element_by_xpath(f"//div[contains(text(), '{date[0]}')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[contains(text(), 'День')]").click()
        time.sleep(1)
        driver.find_element_by_xpath(f"//div[contains(text(), '{date[1]}')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[contains(text(), 'Год')]").click()
        time.sleep(1)
        driver.find_element_by_xpath(f"//div[contains(text(), '{date[2]}')]").click()
        time.sleep(1)
        email = driver.find_element_by_xpath("//input[@name='email']")
        email.send_keys("vagefe2667@mustbeit.com")
        time.sleep(1)
        email = driver.find_element_by_xpath("//input[@autocomplete='new-password']")
        email.send_keys(getPassword())
        driver.find_element_by_xpath("//*[@stroke='#161823']").click()
        time.sleep(10)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()