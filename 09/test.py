from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")
#
# input = driver.find_element_by_css_selector('#kw')
# input.send_keys("苍老师照片")

# button = driver.find_element_by_css_selector('#su')
# button.click()
from selenium import webdriver
from selenium.webdriver.common.by import By


# 登陆百度
def main():
    global driver
    # chromedriver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    # driver = webdriver.Chrome()
    # # 打开页面
    # page = driver.get('https://www.baidu.com/')
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")

    input = driver.find_element(By.ID, 'kw')
    input.send_keys("马保国")
    #
    # button = driver.find_element_by_css_selector('#su')
    button = driver.find_element(By.ID, 'su')

    button.click()

    currentUrl = driver.current_url
    print(currentUrl)


if __name__ == "__main__":
    main()

input()
