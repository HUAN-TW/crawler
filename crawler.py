from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://www.skyscanner.com.tw/transport/flights/tpet/tyoa/231102/231107/?adultsv2=1&cabinclass=economy&childrenv2=&inboundaltsenabled=false&outboundaltsenabled=false&preferdirects=true')

soup = BeautifulSoup(driver.page_source, 'lxml')


# specific_elements = soup.find_all(
#     'div', class_='content-wrap')
# print(specific_elements)
print(soup)
