from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')

driver.get('https://fabrykatestow.pl/')
driver.maximize_window()

driver.find_element_by_id('menu-item-622').click()

driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section/div[2]/div/div/div/div/section[1]/div/div/div[1]/div/div/div/div/div/a').click()

element = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div/div/section[5]/div[2]/div/div/div')

driver.execute_script("arguments[0].scrollIntoView(true);", element)

driver.save_screenshot('KimJestTwojInstruktor.png')

driver.quit()