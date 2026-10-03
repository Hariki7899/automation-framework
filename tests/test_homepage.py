from selenium import webdriver
from selenium.webdriver.common.by import By

#urls:
home_page_url='https://www.automationexercise.com/'

#locators
homepage_title="//div[@class='logo pull-left']/a/img"
home_navigation_button="//div[@class='shop-menu pull-right']/ul/li/a/i[@class='fa fa-home']"
category_title_text="//div[@class='left-sidebar']/h2/text()"
category_women="(//div[@class='panel-heading']/h4/a)[1]"
polo_brand="//div[@class='brands-name']/ul/li/a[text()='Polo']"


#Test_cases
def test_homepage_01():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(home_page_url)
    home_page_title_element=driver.find_element(By.XPATH,homepage_title)
    home_page_title_text=home_page_title_element.get_attribute('alt')
    assert home_page_title_text == 'Website for automation practice'
    page_title=driver.title
    assert page_title == 'Automation Exercise'
    driver.quit()