import requests
import re
from spider import Spider

result = Spider('Spider_X', 'https://dp.nifa.org.cn/HomePage?method=getTargetProjectInfo&sorganation=911101055548793445&stheonlyid=911101055548793445', 3708541, 2, '&sdebtortypeb=01&sfullnames=911101055548793445')
print(result.get_list())