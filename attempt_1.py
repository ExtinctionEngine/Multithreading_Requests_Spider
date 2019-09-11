import requests
import re
from lxml import etree
from lxml import html

url = 'https://dp.nifa.org.cn/HomePage?method=getTargetProjectInfo&sorganation=911101055548793445&stheonlyid=9111010555487934453591015&sdebtortypeb=01&sfullnames=911101055548793445'
raw_content = requests.get(url).text
match_pattern = r'<td(.*?)</td>'
level_1_soup_list = re.findall(match_pattern, raw_content, re.S|re.M)
level_2_soup_list = []
i = -1
for level_1_soup in level_1_soup_list:
    i += 1
    level_2_soup = level_1_soup.split('>')[1]
    # print(i, level_2_soup)
    level_2_soup_list.append(level_2_soup)

project_name = level_2_soup_list[1]
project_number = level_2_soup_list[3]
project_intro = level_2_soup_list[5]
project_link = level_2_soup_list[7].split('\"')[1]  # Special Design
project_purpose = level_2_soup_list[9]
project_size = level_2_soup_list[11]
project_duration = level_2_soup_list[13]
project_apr = level_2_soup_list[15]
project_repay_start = level_2_soup_list[17]
project_repay_method = level_2_soup_list[19].strip()  # Special Design
project_repay_details = level_2_soup_list[21]
project_status = level_2_soup_list[23].strip()  # Special Design
project_raise_start = level_2_soup_list[25]
project_guarantee = level_2_soup_list[27]
project_repay_source = level_2_soup_list[29]
project_risk = level_2_soup_list[31]
project_expense = level_2_soup_list[33]
project_template_number = level_2_soup_list[35]
project_lender_notice = level_2_soup_list[37]
project_borrower_type = level_2_soup_list[39].strip()  # Special Design
project_borrower_name = level_2_soup_list[43]
project_document_type = level_2_soup_list[45].strip()  # Special Design
project_document_number = level_2_soup_list[47]
project_borrower_job = level_2_soup_list[49]
project_borrower_other_info = level_2_soup_list[51]
project_borrower_credit = level_2_soup_list[53]
project_borrower_default_times = level_2_soup_list[55]
project_borrower_default_amounts = level_2_soup_list[57]
project_borrower_income_and_debt = level_2_soup_list[59]

list_of_attribute = [project_name, project_number, project_intro, project_link, project_purpose, project_size,
                     project_duration, project_apr, project_repay_start, project_repay_method, project_repay_details,
                     project_status, project_raise_start, project_guarantee, project_repay_source, project_risk,
                     project_expense, project_template_number, project_lender_notice, project_borrower_type, project_borrower_name,
                     project_document_type, project_document_number, project_borrower_job, project_borrower_other_info,
                     project_borrower_credit, project_borrower_default_times, project_borrower_default_amounts, project_borrower_income_and_debt]

print(list_of_attribute)
