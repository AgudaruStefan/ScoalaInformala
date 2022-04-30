from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.emag.ro/#opensearch")
get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()

def browser_function():
    driver_path = "path/to/chromedriver"
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(driver_path, options=chr_options)
    chr_driver.get("https://target_website.com")

for i in range(1, 62):
    search_element = browser.find_element(by=By.CLASS_NAME, value='list-view-updated')
    print(search_element.text)
    print('+++++++++++++++++++++++++++++++')
