from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
departure_date = '2023-10-25'
return_date = '2023-11-01'
url = f'https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY&city=TYO&departure={departure_date}&backdate={return_date}&type=ROU&airline%5B%5D=none&bclass=EC&forward%5B%5D=NSTOP&sort=price&order=up&lcc=on'

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)
print(url)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

specific_elements = soup.find_all('div', id='result_area')

for element in specific_elements:
    with open('raw.file', 'w') as file:
        text_content = element.get_text()
        lines = text_content.split('\n')
        for line in lines:
            if line.strip() and "選擇" not in line and "機票" not in line:
                file.write(line.strip() + '\n')


with open('raw.file', 'r') as file:
    lines = file.readlines()

data = []
current_data = []

for line in lines:
    line = line.strip()
    if line:
        current_data.append(line)
        if len(current_data) == 12:
            data.append(current_data)
            current_data = []

selected_data = data[:3]

for entry in selected_data:
    print("航空公司:", entry[0])
    print("去程啟程時間:", entry[1])
    print("去程飛行時間:", entry[2])
    print("去程抵達時間:", entry[3])
    print("去程出發機場:", entry[4])
    print("去程抵達機場:", entry[5])
    print("回程啟程時間:", entry[6])
    print("回程飛行時間:", entry[7])
    print("回程抵達時間:", entry[8])
    print("回程出發機場:", entry[9])
    print("回程抵達機場:", entry[10])
    print("價格:", entry[11])
    print("\n")
