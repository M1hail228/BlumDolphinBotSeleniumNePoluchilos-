from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import time
import random

profile_id = ['37729833', '37745661', '37745677', '37745661', '37754785', '44886385', '44886385', '44886412', '44886427', '44886442']

while True:
    try:
        for item in profile_id: 
            try:
                req_url = 'http://localhost:3001/v1.0/browser_profiles/'+ item +'/start?automation=1'
                response = requests.get(req_url)
                response_json = response.json()
                print(response_json)

                port = str(response_json['automation']['port'])
                print(port)

                chrome_driver = Service('C:/Users/User/PyCharm Projects/Dolphin автоматизация/chromedriver.exe')
                options = webdriver.ChromeOptions()
                options.debugger_address = '127.0.0.1:' + port

                driver = webdriver.Chrome(service=chrome_driver, options=options)

                driver.get('https://web.telegram.org/k/#@BlumCryptoBot')
                time.sleep(20)

                element = driver.find_element(By.XPATH, '//*[@id="column-center"]/div/div/div[3]/div[2]/div/section/div[6]/div/div/div[2]/div[1]/button')  
                element.click()
                time.sleep(10)

                element = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[3]/div')
                element.click()
                time.sleep(10)

                element = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[3]/div/button') 
                element.click()
                time.sleep(10)

                element = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[3]/div/button/div[2]') 
                element.click()
                time.sleep(5)

                driver.close()

            except Exception as e:
                print(f"An error occurred: {e}")
                driver.quit()
                pass

            # Внутренние элементы выполнены, даем задержку перед следующей итерацией
            wait_time_inner = random.randint(5*1, 8*1)
            print(f"Waiting for {wait_time_inner} seconds before next iteration...")
            time.sleep(wait_time_inner)

    except Exception as e:
        print(f"An error occurred: {e}")
        pass

    # Все итерации выполнены, ждем перед следующим выполнением цикла
    wait_time_outer = 8 * 3600 + (10 * 3600 - 8 * 3600) * random.random()
    print(f"Waiting for {wait_time_outer} seconds before next cycle...")
    time.sleep(wait_time_outer)

