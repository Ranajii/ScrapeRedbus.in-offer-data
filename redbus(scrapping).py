############################
'''https://www.redbus.in/info/OfferTerms'''

# REDBUS #

from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
driver = webdriver.Chrome(r"C:\Users\visha\chromedriver")


url = 'https://www.redbus.in/info/OfferTerms'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

# Using Chrome to access web


#driver.get(url)
#driver.find_element_by_xpath('''//*[@id="mBWrapper"]/table/tbody/tr[1]/td[1]''').click()
#driver.back()
#
#driver.forward()
#driver.find_element_by_xpath('''//*[@id="mBWrapper"]/table/tbody/tr[1]/td[2]''').click()

driver.get(url)
termsbox = '//*[@id="mBWrapper"]/table/tbody/tr[1]/td[1]'
collect = []
for j in range(1,6):
    for i in range(1,4):
        offernum = str('Offer ')+str(j)+'-'+str(i)
        rowise = termsbox[0:-8]+str(j)+termsbox[-7:-2]+str(i)+']'
        driver.find_element_by_xpath(rowise).click()
        time.sleep(3)
        offername = driver.find_element_by_id('OfferDiscription').text
        print(offername)
        linknew = driver.find_element_by_class_name('terms').text
        print(linknew)
        driver.back()
        driver.forward()
        collect.extend([[offernum,offername,linknew]])
        

############################
'for 1 link'
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
driver = webdriver.Chrome(r"C:\Users\visha\chromedriver")


url = 'https://www.redbus.in/info/OfferTerms'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
driver.get(url)
termsbox = '//*[@id="mBWrapper"]/table/tbody/tr[1]/td[1]'
driver.find_element_by_xpath(termsbox).click()
name = driver.find_element_by_id('OfferDiscription').text




