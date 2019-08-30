import requests
import re
from spider import Spider

# url = 'https://dp.nifa.org.cn/HomePage?method=getTargetProjectInfo&sorganation=911101055548793445&stheonlyid=9111010555487934453591015&sdebtortypeb=01&sfullnames=911101055548793445'
# raw_content = requests.get(url).text
# res_tr = r'<td(.*?)</td>'
# m_str = re.findall(res_tr, raw_content, re.S|re.M)
# print(type(m_str))
# for line in m_str:
#     target = line.split('>')[1]
#     print(target)

# string = "<a href=\"https://www.renrendai.com/loan-3591015.html\" "
# soup = string.split('\"')[1]
# print(soup)
#
# string = '''
#
#
#
#
#
#
#
#
#
#
#
# 							                		按月等额本息还款
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 							                '''
# soup = string.strip()
# print(soup)

result = Spider('Spider_X', 'https://dp.nifa.org.cn/HomePage?method=getTargetProjectInfo&sorganation=911101055548793445&stheonlyid=911101055548793445', 3708541, 2, '&sdebtortypeb=01&sfullnames=911101055548793445')
print(result.get_list())