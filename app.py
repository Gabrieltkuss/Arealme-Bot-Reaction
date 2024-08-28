from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def executar_codigo():
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.get('https://www.arealme.com/reaction-test/pt/')
    sleep(2)
    
    firststep = driver.find_element(By.XPATH,"//button[@class='progress-button pure-button pure-button-primary']")
    firststep.click()
    sleep(2)

    secstep = driver.find_element(By.XPATH,"//div[@class='click_desc blink_me']")
    secstep.click()
    sleep(1)

    while True:
        try:
            thirdstep = driver.find_element(By.XPATH, "//div[@class='tfny-circleGreen']")
            thirdstep.click()
            sleep(0.1)
        except NoSuchElementException:
            print("Botão verde não encontrado. Tentando novamente...")


executar_codigo()