from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
# to wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# jobs page
import data_extraction as de

# don't change the size
chrome_options = Options()
chrome_options.add_argument("--start-maximized")


location = "path to selenium webdriver"
driver = webdriver.Chrome(
    executable_path=location, chrome_options=chrome_options)

# eg:
# driver = webdriver.Chrome(
#     executable_path="D:\Downloads2\chromedriver_win32/chromedriver", chrome_options=chrome_options)


def switch_win():
    j = driver.window_handles
    for i in j:
        if(i != home_page):
            driver.switch_to.window(i)
            break


def return_home():
    driver.close()
    driver.switch_to.window(home_page)


# can also change the keyword(python in this case)
number_of_pages = 3
flag = True
for i in range(2, number_of_pages+1):
    var = str(i)
    url = "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence="+var+"&startPage=1"
    # opens the given url
    driver.get(url)
    home_page = driver.current_window_handle
    if flag == True:
        # to close the pop up
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="closeSpanId"]')))
        element.click()

        # to accept cookies
        driver.find_element_by_xpath(
            '//*[@id="site"]/div[6]/div/div[2]/button').click()
        flag = False
    # to get all the div tags of the jobs
    li = driver.find_elements_by_xpath(
        '//*[@id="searchResultData"]/ul/li/header/h2/a/strong')
    for i in li:
        i.click()
        switch_win()
        # call the beautiful soup function
        job_url = driver.current_url
        de.jobs(job_url)
        time.sleep(1)
        return_home()
        time.sleep(1)

    # call the beautiful soup function
