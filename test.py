
from src.fume_spider import FumeSpider
from src.database.save_to_database import Fume_writer
from src.url.url_parser import Url,Url_params
from src.login import *
from src.survey.extract import Extract
from src.request_.request_test_data import LocalFumePage
from src.request_.request import RemoteFumePage
from src.util.generate_url import GenerateUrl
from src.config import config

def main():
    local_fume_page = LocalFumePage()
    remote_fume_page = RemoteFumePage()
    f_s = FumeSpider()
    # 请求本地网页
    html = f_s.fetch('https://111',local_fume_page)

    # 请求远程网页
    # html = f_s.fetch('https://111',remote_fume_page)


    fume_sum = Extract.extract_from_html(html)
    print(f'爬取总数为：{fume_sum}')
    #写入数据库
    Fume_writer.writer(fume_sum)

if __name__ == '__main__':
    # main()
    for url in GenerateUrl.generate_url(config['development'].shop_name):
        print(url)