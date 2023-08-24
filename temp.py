
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
from bs4 import BeautifulSoup

ptrn = "https://[\w./-]+"
driver = webdriver.Chrome()
# driver.maximize_window()
inner_driver = webdriver.Chrome()
# inner_driver.minimize_window()
url = "https://www.chinabidding.com/en"
driver.get(url)
time.sleep(5)
xpath = '//*[@id="bidding"]/div[2]/div[2]/ul/li[2]/a'
elem = driver.find_element(By.XPATH, xpath)
elem.click()
time.sleep(2)
xpath_button='//*[@id="bidding"]/div[2]/div[3]/div[1]/div[2]'
while True:
    try:
        button = driver.find_element(By.XPATH,xpath_button)
        button.click()
        time.sleep(5)
    except:
        break

X_path_tenders = '//*[@id="bidding"]/div[2]/div[3]/div[1]/ul/li'
elements = driver.find_elements(By.XPATH, X_path_tenders)
# print(elements)
print(len(elements))

# 
for ele in elements:
    abc = ele.get_attribute("innerHTML")
    aa = re.findall(ptrn, abc)
    if len(aa)>0:
        inner_driver.get(aa[0])
        dd='//*[@id="bidding"]/div[3]/div/div[4]'

        try:
            main_element = inner_driver.find_element(By.XPATH,dd)
            main_text = main_element.get_attribute("innerHTML")
            # print(main_text)
            ptrn_loan_number = r"Loan Number :[\w.-]+"
            ptrn_bidding_no = r"Bidding No :[\w.-]+"
            ptrn_bidding_agency = r"Bidding Agency :[\w\s.,]+"
            ptrn_purchasers = r"Purchasers :[\w\s&;.,]+"
            ptrn_bidding_type = r"Bidding Type :[\w\s]+"
            ptrn_deadline_for_submitting = r"Deadline for Submitting Bids :[\w-]+"
            loan_no = re.search(ptrn_loan_number, main_text).group()
            bidding_no = re.search(ptrn_bidding_no, main_text).group()
            bidding_agency = re.search(ptrn_bidding_agency, main_text).group()
            purchasers = re.search(ptrn_purchasers, main_text).group()
            bidding_type = re.search(ptrn_bidding_type, main_text).group()
            deadline = re.search(ptrn_deadline_for_submitting, main_text).group()
            print(loan_no,bidding_no,bidding_agency,purchasers,bidding_type,deadline, sep="\n")
            print()

        except:
            pass



    time.sleep(3)

time.sleep(5)
driver.close()