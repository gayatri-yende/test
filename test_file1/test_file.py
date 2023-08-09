import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

class Test_py:
    def test_google(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com/")
        logo = driver.find_element(By.CLASS_NAME, "lnXdpd").is_displayed()
        print(logo)
        if logo == True:
            driver.close()
            assert True
        else:
            driver.close()
            assert False

    def test_credence(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://credence.in/")
        offer = driver.find_element(By.XPATH, "//div[@class='elementor-container elementor-column-gap-no']//marquee").text
        print(offer)
        print(driver.title)
        if driver.title == "Credence":
            driver.close()
            assert True
        else:
            driver.close()
            assert False

    def test_contact(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://credence.in/")
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
        time.sleep(4)
        l = len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p/a"))
        time.sleep(2)
        print(l)
        list = []
        for r in range (1, l+1):
            contact = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p/a["+str(r)+"]").text
            list.append(contact)
            print(list)
        if "+91 9091929355" in list:
            print("contact is present")
            print(list.index("+91 9091929355"))
            assert True
            # break
        else:
            print("contact is not present")
            assert False



