from housekeeping import *
import threading
from queue import Queue
import spider
import time

PROJECT_NAME = 'renrendai_4'
PROJECT_URL_1 = 'https://dp.nifa.org.cn/HomePage?method=getTargetProjectInfo&sorganation=911101055548793445&stheonlyid=911101055548793445'
PROJECT_CSV_HEADER = ['URL_key', '项目名称', '项目编号', '项目简介', '项目销售链接', '借款用途', '借款金额（元）', '借款期限', '年化利率',
                      '预计起息日', '还款方式', '还款方式说明', '项目状态', '募集开始时间', '还款保障措施', '还款来源',
                      '项目风险评估', '相关费用', '合同模板号', '出借人适当性管理提示', '借款方类型', '姓名', '证件类型',
                      '证件号码', '工作性质', '其他借款信息', '借款人征信报告情况', '在本平台逾期次数', '在本平台逾期总金额（元）',
                      '借款人收入及负债情况']
PROJECT_INITIAL_NUM = 3707813
PROJECT_MAX_PAGES = 100000
PROJECT_URL_2 = '&sdebtortypeb=01&sfullnames=911101055548793445'
NUMBER_OF_SPIDERS = 12
queue = Queue()

create_data_csv(PROJECT_NAME)
set_csv_header(PROJECT_NAME, PROJECT_CSV_HEADER)
iterator_set = create_iterator_set(PROJECT_MAX_PAGES)


def create_spiders():
    for _ in range(NUMBER_OF_SPIDERS):
        t = threading.Thread(target=work, daemon=True)
        t.start()


def work():
    while True:
        # time.sleep(2)
        iterator = queue.get()  # when get() is proceed, it blocks and waits until queue has something to return
        record = spider.Spider(threading.current_thread().name, PROJECT_URL_1, PROJECT_INITIAL_NUM, iterator, PROJECT_URL_2)
        if record.get_list()[1] != 'FAIL':
            with open(PROJECT_NAME + '.csv', 'a', encoding="utf-8") as table:
                for attribute in record.get_list():
                    table.write(str(attribute))
                    table.write('\t')
                table.write('\n')
            iterator_set.remove(iterator)
            print('Queue ' + str(len(iterator_set)) + ' | Crawled ' + str(PROJECT_MAX_PAGES-len(iterator_set)))
            queue.task_done()
        else:
            print('Queue ' + str(len(iterator_set)) + ' | Crawled ' + str(PROJECT_MAX_PAGES - len(iterator_set)))
            # queue.task_done()


def create_jobs():
    for iterator in iterator_set:
        queue.put(iterator)
    queue.join()  # to ensure that jobs are done one by one
    checker()


def checker():
    # queued_iterator = create_iterator_set(PROJECT_MAX_PAGES)
    if len(iterator_set) > 0:
        print(str(len(iterator_set)) + ' urls in the queue')
        create_jobs()


start_time = time.time()
create_spiders()
checker()
end_time = time.time()
print(end_time - start_time)


