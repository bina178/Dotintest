from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
path = os.path.dirname(os.path.abspath(__file__))
address = os.path.join(path , 'chromedriver.exe')
driver = webdriver.Chrome(executable_path= address)
driver.maximize_window()

driver.get("https://www.digikala.com/")

driver.find_element_by_xpath("//a[contains(@href,'/users/login-register') and contains(text(),'ورود')]").click()
driver.find_element_by_name('login[email_phone]').send_keys('09129349744')
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_element_by_name('login[password]').send_keys('123456')
driver.find_element_by_xpath("//button[@type='submit']").click()

driver.find_element_by_xpath("//div[contains(@class,'btn-user-container')]/a").click()
time.sleep(2)

driver.find_element_by_xpath("//div[@class='c-navi-new-list__category c-navi-new-list__category--main']").click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="categories-1"]/ul/li[36]/a[1]').click()

driver.execute_script("window.scrollTo(0, 500)")  

time.sleep(3)
driver.find_element_by_xpath("//label[@data-search='اپل Apple']").click()



driver.execute_script("window.scrollTo(0, -500)") 
time.sleep(3)
driver.find_element_by_xpath("//a[text()='جدیدترین']").click()

driver.execute_script("window.scrollTo(0, 400)")  
time.sleep(5)
driver.find_element_by_xpath("(//a[@class='js-product-url'])[6]").click()

time.sleep(5)
driver.switch_to_window(1)

driver.find_element_by_xpath("//a[contains(@class,'js-ab-product-action') and child::span]").click()
