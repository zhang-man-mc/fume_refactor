
from src.fume_spider import FumeSpider
from src.database.save_to_database import Fume_writer
from src.url.url_parser import Url,Url_params
from src.login import *
from src.survey.extract import Extract
from src.request_.request_test_data import LocalFumePage
from src.request_.request import RemoteFumePage
from src.util.generate_url import GenerateUrl
from src.config import config
from src.decrator import loop_get_data_by_shop

# 测试获取本地和远程数据
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


# 测试装饰器
@loop_get_data_by_shop(shops=['吉刻联盟','大成海鲜'])
def add(url,page,*args,**kwargs):
    print("加法函数被调用了")
    print(url)
    print(f"page:{page}")
    return url

if __name__ == '__main__':
    # main()

    # 测试生成url
    # for url in GenerateUrl.generate_url(config['development'].shop_name):
    #     print(url)

    # 测试装饰器
    add(5)

    # 测试装饰器修饰类方法
