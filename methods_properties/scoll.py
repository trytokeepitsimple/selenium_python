from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class Scroll():

    def run(self):
        baseURL = 'https://www.letskodeit.com/practice'
        service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)

        #scrolldown

        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(3)
        print("Scrolled Down Fully")

        #scrollup
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(3)
        print("Scrollup Fully")


        #scroll_element into view
        element= driver.find_element(By.ID,"mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);",element)
        time.sleep(3)
        #move up a bit by scrolling up so that we can see the element
        driver.execute_script("window.scrollBy(0,-150);")
        time.sleep(2)


        #native way to scroll element into view

        driver.execute_script("window.scrollBy(0,-1000);") #for reseting everything as it is
        location = element.location_once_scrolled_into_view # selenium method
        print("Location is "+str(location))
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-150);")
        time.sleep(1)


        driver.quit()



sc = Scroll()
sc.run()