from selenium.webdriver.common.by import By

#locators
homepage_logo = "//div[@class='logo pull-left']/a/img"
home_navigation_button = "//div[@class='shop-menu pull-right']/ul/li/a/i[@class='fa fa-home']"
category_title = "//div[@class='left-sidebar']/h2"
category_women = "(//div[@class='panel-heading']/h4/a)[1]"
category_list = "//div[@class='panel-heading']/h4/a"
polo_brand = "//div[@class='brands-name']/ul/li/a[text()='Polo']"

#Test_cases
def test_homepage_basic(driver):
    home_page_logo_element = driver.find_element(By.XPATH,homepage_logo)
    home_page_title_text = home_page_logo_element.get_attribute('alt')
    assert home_page_title_text == 'Website for automation practice'
    page_title=driver.title
    assert page_title == 'Automation Exercise'

def test_category_section(driver):
    category_title_text = driver.find_element(By.XPATH,category_title).text
    assert category_title_text == 'CATEGORY'
    cate_list_elements = driver.find_elements(By.XPATH,category_list)
    assert len(cate_list_elements) == 3