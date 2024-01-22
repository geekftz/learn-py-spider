from telnetlib import EC
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()

driver.get("https://www.bilibili.com/")
WAIT = WebDriverWait(driver, 10)


# 登陆百度
def main():
    global driver
    # chromedriver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    # driver = webdriver.Chrome()
    # # 打开页面
    # page = driver.get('https://www.baidu.com/')

    input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-search-content > input")))
    submit = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.nav-search-btn')))

    # 被那个破登录遮住了
    # index = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#primary_menu > ul > li.home > a")))
    # index.click()

    input.send_keys('蔡徐坤 篮球')
    submit.click()

    print('跳转到新窗口')
    all_h = driver.window_handles
    driver.switch_to.window(all_h[1])
    # 获取数据
    # get_source()

    total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                       ".vui_pagenation--btns > button:nth-last-child(2)")))

    totalNum = int(total.text)

    print(totalNum)

    # for i in range(2, int(total + 1)):
    #     next_page(i)


def next_page(page_num):
    print('获取下一页数据')
    next_btn = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                      '#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.next > button')))
    next_btn.click()
    WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                 '#server-search-app > div.contain > div.body-contain > div > div.page-wrap > div > ul > li.page-item.active > button'),
                                                str(page_num)))


if __name__ == "__main__":
    main()
    # print(sys.version)
# input()
