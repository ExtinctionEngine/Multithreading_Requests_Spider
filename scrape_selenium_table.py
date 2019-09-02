import csv
from selenium import webdriver

MAX_PAGE_NUM = 16

with open('platforms_info_table.csv', 'w', encoding="utf-8") as table:
    csv_writer = csv.writer(table, delimiter='\t')
    csv_writer.writerow(['机构名称','累计借款金额（万元）','累计借款笔数（笔）','累计借款人数量（人）','累计出借人数量（人）','项目逾期率','金额逾期率'])

driver = webdriver.Chrome()

for i in range(1, MAX_PAGE_NUM + 1):
    url = "https://dp.nifa.org.cn/HomePage?method=getOperateInfo&currentPage=" + str(i)

    driver.get(url)

    names = driver.find_elements_by_xpath('//div[@class="mouseover-charts"]//p')
    money_amounts = driver.find_elements_by_xpath('//tbody[@id="runinfotbody"]//tr//td[2]')
    projects_amounts = driver.find_elements_by_xpath('//tbody[@id="runinfotbody"]//tr//td[3]')
    borrowers_amounts = driver.find_elements_by_xpath('//tbody[@id="runinfotbody"]//tr//td[4]')
    lenders_amounts = driver.find_elements_by_xpath('//tbody[@id="runinfotbody"]//tr//td[5]')
    projects_default_rates = driver.find_elements_by_xpath('//tbody[@id="runinfotbody"]//tr//td[6]')
    money_default_rates = driver.find_elements_by_xpath('//tbody[@id="runinfotbody"]//tr//td[7]')

    num_page_items = len(names)
    with open('platforms_info_table.csv', 'a', encoding="utf-8") as table:
        for i in range(num_page_items):
            table.write(names[i].text + "\t" + money_amounts[i].text + "\t" + projects_amounts[i].text + "\t"
                        + borrowers_amounts[i].text + "\t" + lenders_amounts[i].text + "\t"
                        + projects_default_rates[i].text + "\t" + money_default_rates[i].text + "\n")

# Clean up (close browser once task is completed.)
driver.close()
