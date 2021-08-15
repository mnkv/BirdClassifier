from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import base64
import requests


# Recording images from search
def creative_commons(driver):
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[2]/div[2]/div/div').click()
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/c-wiz[1]/div/div/div[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/c-wiz[1]/div/div/div[3]/div/a[1]/div/span').click()
    time.sleep(1)

def define_driver(input):
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')

    box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    box.send_keys(input)
    box.send_keys(Keys.ENTER)

    driver.find_element_by_xpath('//*[@id="L2AGLb"]/div').click()
    driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
    #creative_commons(driver)

    time.sleep(1)


    #Will keep scrolling down the webpage until it cannot scroll no more
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(1)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element_by_xpath('//*[@id="REsRA"]').click()
            time.sleep(1)

            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1)
            new_height = driver.execute_script('return document.body.scrollHeight')
            try:
                driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[3]/div[2]/input').click()
                time.sleep(5)
            except:
                pass  

        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height

    return driver    
def record_images(driver, min, max, img_filename):
    for i in range(min, max):
        try:
            a = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').get_attribute('src')
            substring = "base64"
            filename = img_filename + str(i)  + '.jpg'

            if a.find(substring) != -1: 
                a = a.replace("data:image/jpeg;base64,", "")
                imgdata = base64.b64decode(a)
                
                with open(filename, 'wb') as f:
                    f.write(imgdata) 
                # https://pythonspot.com/selenium-get-images/
            else: 
                r = requests.get(a, allow_redirects=True)
                open(filename, 'wb').write(r.content)  
        except:
            pass

    driver.close()


if __name__ == '__main__':
    results_folder = r'C:\Users\ksesh\files\Documents\BirdClassifierUK\training\dogs\\'
    driver = define_driver('dog')
    record_images(driver, 2, 5000, results_folder+'dog5')
 