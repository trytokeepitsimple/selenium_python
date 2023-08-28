from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FFService

class RunFFTests():

    def test(self):
        #ff_service = FFService(executable_path="../drivers/geckodriver-v0.33.0-linux64/geckodriver")
        # Instantiate Browser
        driver = webdriver.Firefox(executable_path="../drivers/geckodriver-v0.33.0-linux64/geckodriver")
        # Open provided URL
        driver.get("https://www.letskodeit.com")


run_tests = RunFFTests()
run_tests.test()