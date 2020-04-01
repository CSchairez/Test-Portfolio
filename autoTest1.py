from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def init_driver(drv):
    
    drv.set_page_load_timeout(5)
    drv.get("https://portfolio-e7816.firebaseapp.com/")
    time.sleep(2)

    
def findLinks(drv, xpath_link):
    
    # findLinks function to test all pages except Homepage: "/#" 
    element = drv.find_element_by_xpath(xpath_link)
    drv.execute_script("arguments[0].click();", element)
    drv.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    
def main():
    
    driver = webdriver.Chrome(r"C:\Users\achai\OneDrive\Desktop\Python Files\Testing\Testing\drivers\chromedriver.exe")     # Load driver in main. Will be used 'globally'.
    driver.set_page_load_timeout(10)

    # href links
    resume_page = "(//a[contains(@href, '#/resume')])"
    projects_page = "(//a[contains(@href, '#/projects')])"
    contact_page = "(//a[contains(@href, '#/contact')])"

    # Define actions
    actions = ActionChains(driver) 
    """
    ** Section for testing Github links and opening in new tabs **
    """
    
    init_driver(driver)         # Initialize to load the page.
    time.sleep(3)
    findLinks(driver, resume_page)          # View links to different pages.
    findLinks(driver, projects_page)
    findLinks(driver, contact_page)
    
    driver.quit()


main()
