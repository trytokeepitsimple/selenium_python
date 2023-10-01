from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


class WebElements():

    def run(self):
        baseURL = 'https://www.letskodeit.com/practice'
        service = Service(executable_path='../drivers/chromedriver_linux64/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10);

        login_btn = driver.find_element(By.XPATH, "//a[@href='/login']")
        time.sleep(1)
        login_btn.click()
        print("login btn is clicked , moving forward to login screen")


        user_name_f = driver.find_element(By.XPATH,"//input[@name='email']")
        time.sleep(1)
        user_name_f.send_keys("test@email.com")
        password_name_f = driver.find_element(By.XPATH, "//input[@name='password']")
        time.sleep(1)
        password_name_f.send_keys("abcabc")
        sign_in_btn = driver.find_element(By.ID, 'login')
        time.sleep(2)
        sign_in_btn.click()
        time.sleep(2)
        print("Sign In Button got clicked")


        all_course_link = driver.find_element(By.XPATH,"//a[@href='/courses']")
        time.sleep(2)
        all_course_link.click()


        search_box = driver.find_element(By.XPATH,'//input[@name="course"]')
        print("search box is captured")
        search_box.send_keys("Java")
        search_box_btn= driver.find_element(By.XPATH,"//button[@class='find-course search-course' and contains(@type,'submit')]")
        search_box_btn.click()


        #select course
        _course ="//div[@id='course-list']//h4[contains(text(), '{0}')]"
        _course_selection=_course.format("JavaScript for beginners")
        time.sleep(2)
        selected_course = driver.find_element(By.XPATH,_course_selection)
        time.sleep(2)
        selected_course.click()
        time.sleep(2)
        print("Javascript Course got selected and hence our journey comes to an end")
        driver.quit()




run_element_check = WebElements()
run_element_check.run()